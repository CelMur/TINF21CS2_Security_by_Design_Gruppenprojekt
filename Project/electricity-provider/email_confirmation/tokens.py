import secrets
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            secrets.token_hex(20)
        )

account_activation_token = AccountActivationTokenGenerator()