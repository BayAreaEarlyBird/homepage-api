from django.contrib.auth.hashers import check_password

from auth.exceptions import AuthenticationError
from auth.utils import jwt_decode, jwt_get_username_from_claims, jwt_claims_builder, jwt_encode
from user.models import User


def authenticate(**kwargs):
    """ Authenticates using the given token.

    Args:
        **kwargs: A dict containing authentication information.
        e.g.:
        {
            "username": "hello",
            "password": "earlybird"
        }

    Returns:
        user: The corresponding user object.
    """
    token = kwargs.get('token')

    if token is not None:
        identifier = verify_token(token=token)
    else:
        username = kwargs.get('username')
        password = kwargs.get('password')

        identifier = verify_username_password(username=username,
                                              password=password)

    if identifier is None:
        raise AuthenticationError('Failed to verify the identity.')

    # returns hydrated User object.
    try:
        return User.objects.get(username=identifier)
    except User.DoesNotExist:
        raise AuthenticationError('Requested user does not exist.')


def verify_token(token):
    """ Verifies token.

    Args:
        token: A string representing JWT.

    Returns:
        username: A string extracted from JWT's claims and will be used to
        position the right User object.
    """
    try:
        jwt_claims = jwt_decode(token)
    except:
        raise AuthenticationError('Failed to verify the token.')

    if jwt_claims is not None:
        username = jwt_get_username_from_claims(jwt_claims)
    else:
        raise AuthenticationError('Invalid token.')

    return username


def verify_username_password(username, password):
    """ Verifies user using username and password.

    Args:
         username: A string.
         password: A string (without any encryption).

    Returns:
        username: A string extracted from JWT's claims and will be used to
        position the right User object.
    """
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise AuthenticationError('Requested user does not exist.')

    if not check_password(password, user.password):
        raise AuthenticationError('Wrong username or password.')

    return username


def generate_token(user):
    """ Generates token using the given user object.

    Args:
        user: A user object.

    Returns:
        token: A string representing JWT.
    """
    try:
        claims = jwt_claims_builder(user)
        token = jwt_encode(claims)
    except AttributeError:
        raise AuthenticationError('Failed to generate a token.')

    return token, claims
