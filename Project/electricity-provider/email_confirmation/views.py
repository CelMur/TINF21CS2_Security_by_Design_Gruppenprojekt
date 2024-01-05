from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.http import HttpResponse
from django.views import View
from .tokens import account_activation_token
from django.contrib.auth import get_user_model

from email_confirmation.models import EmailConfirmation
from authentication.models import User
from django.utils import timezone

User = get_user_model()

class ActivateAccountView(View):
    def get(self, request, token, second_token):
        
        try:
            email_confirmation = EmailConfirmation.objects.get(token=token, second_token=second_token)
            user:User = email_confirmation.user
        except:
            return HttpResponse('Activation link is invalid or has expired!')
        
        if email_confirmation and User:
            if email_confirmation.claimed or email_confirmation.has_expired(): 
                return HttpResponse('Activation link is invalid or has expired!')
            
            user.email_verified = True
            user.save()

            email_confirmation.claimed = True
            email_confirmation.claimed_at = timezone.now()
            email_confirmation.save()
            return HttpResponse('Thank you for your email confirmation. Now you can use all features of the website.')
        else:
            return HttpResponse('Activation link is invalid or has expired!')
    