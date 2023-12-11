from django.conf import settings
from rest_framework.authtoken.models import Token

class DebugTokenMiddleware:
    '''
    !!!!SECURITY WARNING!!!!:
    This middleware adds the user's auth token to the response headers.
    It only suposed to be used in development mode (DEBUG == TRUE) for testing purposes
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            token, created = Token.objects.get_or_create(user=request.user)
            response['X-Debug-Token'] = token.key
            response['Access-Control-Expose-Headers'] = 'X-Debug-Token'
        except Exception as e:
            pass
        

        return response