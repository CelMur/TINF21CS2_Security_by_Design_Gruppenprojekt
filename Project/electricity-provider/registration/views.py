from .serializers import UserRegistrationSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction

from django.contrib.auth import get_user_model

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from email_confirmation.tokens import account_activation_token
from email_confirmation.models import EmailConfirmation
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer):
        #Hashing the password before saving the user
       
        user = serializer.save(password=serializer.validated_data['password'])

        email_confirmation = EmailConfirmation.objects.create(
            user=user,
            token=account_activation_token.make_token(user),
            second_token=account_activation_token.make_token(user),
            action="account_verification",
            )

        # Send confirmation email
        mail_subject = "Account Verification"
        message = render_to_string("account_activation_email.html", {
            'user': user,
            'domain': get_current_site(self.request).domain,
            'token': email_confirmation.token,
            'second_token': email_confirmation.second_token,
        })

        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])