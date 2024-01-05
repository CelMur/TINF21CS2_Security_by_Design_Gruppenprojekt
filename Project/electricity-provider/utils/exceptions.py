from rest_framework.exceptions import APIException

class AccountNotVerifiedException(APIException):
    status_code = 400
    default_detail = {"error": "Account is not verified yet."}
    default_code = 'account_not_verified'

