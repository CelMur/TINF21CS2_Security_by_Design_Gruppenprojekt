from .settings import *  # Import base settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Use a faster password hasher for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Use a simpler session serializer for tests
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'