from functools import wraps

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from .jwt import jwt_build_claim, jwt_encode, jwt_decode
from .jwt import jwt_get_username_from_claims, jwt_get_token_from_info


def verify_password(username, password):
    """
        Verify whether target user exists in the database and
    password is correct or not.

        Args:
            username: username for target user, str
            password: password for target user, str

        Return:
            whether target user exists in the database and password
        is correct or not, bool
    """
    users = User.objects.filter(username=username)
    return len(users) > 0 and check_password(password, users[0].password)


def generate_token(user):
    """
        Generate token for target user.

        Args:
            user: target user, User

        Return:
            encoded token, str
    """
    claims = jwt_build_claim(user)
    token = jwt_encode(claims)
    return claims, token


def verify_token(token):
    """
        Verify the token is valid or not. Return the username
    if the token is valid.

        Args:
            token: token to be validated, str

        Return:
            username for this token, str
    """
    try:
        claims = jwt_decode(token)
    except:
        return None
    return jwt_get_username_from_claims(claims)


def token_required(func):
    """
        Decorator for token authentication.
    """
    @wraps(func)
    def wrapper(cls, info, **kwargs):
        # get token
        token = jwt_get_token_from_info(info)
        # verify token and get username
        username = verify_token(token)
        users = User.objects.filter(username=username)
        if len(users) > 0:
            return func(cls, info, user=users[0], **kwargs)
        else:
            return None
    return wrapper
