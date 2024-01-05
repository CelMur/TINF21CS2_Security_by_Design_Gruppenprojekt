import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.db.models import F
from django.contrib.auth import authenticate, login
from email_failed_logins.models import EmailFailedLogins
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings


from utils.logger import *

from .serializers import UserAuthenticationSerializer

class UserAuthenticationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request=request, username=username, password=password)

        
        
        
        if user is not None:
            login(request, user)
            user.failed_login_attempts = 0
            user.save(update_fields=['failed_login_attempts'])
            serializer = UserAuthenticationSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if username is not None:
                user = get_user_model().objects.filter(email=username).first()
                user.failed_login_attempts = F('failed_login_attempts') + 1
                user.save(update_fields=['failed_login_attempts'])
                user.refresh_from_db()
                #masking of the username to prevent information leakage in the logs
                hashed_username = hashlib.sha256(username.encode('utf-8')).hexdigest()
                logger.warn(f'failed authentication for user {hashed_username}')
                if user and user.failed_login_attempts > 5:
                    # Send confirmation email
                    mail_subject = "Failed Login Attempts"
                    message = render_to_string("account_failed_logins_email.html", {
                    'user': user,
                    'domain': get_current_site(self.request).domain
                    })
                    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])
                    user.failed_login_attempts = 0
                    user.save(update_fields=['failed_login_attempts'])
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
