from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from jose import jwt

from auth.utils import jwt_get_token, jwt_decode, jwt_get_username_from_claims


class JWTBackend:
    def authenticate(self, request, **kwargs):
        token = jwt_get_token(request)
        if token is None:
            token = kwargs.get('token')
        username = kwargs.get('username')
        password = kwargs.get('password')

        if token is not None:
            try:
                jwt_claims = jwt_decode(token)
            except jwt.ExpiredSignatureError:
                jwt_claims = None
            except jwt.JWTError:
                jwt_claims = None
            except jwt.JWTClaimsError:
                jwt_claims = None

            if jwt_claims is not None:
                username = jwt_get_username_from_claims(jwt_claims)
            else:
                return None

        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

            if not check_password(password, user.password):
                return None

        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
