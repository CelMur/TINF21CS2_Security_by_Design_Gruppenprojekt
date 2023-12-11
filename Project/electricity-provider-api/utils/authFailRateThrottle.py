import hashlib
from rest_framework.throttling import SimpleRateThrottle

from utils.logger import *

class AuthFailRateThrottle(SimpleRateThrottle):
    '''
    Supposed to throttle login attempts after 5 failed attempts in 5 minutes

    But:
        it doesn't work yet >:(
    '''

    scope = 'login_fail'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return None  # Only throttle unauthenticated requests
        
        username = request.data.get('username')
        #masking of the username to prevent information leakage in the logs
        hashed_username = hashlib.sha256(username.encode('utf-8')).hexdigest()

        logger.warning(f'failed authentication for user {hashed_username}')

        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }