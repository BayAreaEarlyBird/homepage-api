from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from jose import jwt

from auth.utils import jwt_decode, jwt_get_username_from_claims, jwt_claims_builder, jwt_encode


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
        return None

    # returns hydrated User object.
    try:
        return User.objects.get(username=identifier)
    except User.DoesNotExist:
        return None


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
    except jwt.ExpiredSignatureError:
        jwt_claims = None
    except jwt.JWTError:
        jwt_claims = None
    except jwt.JWTClaimsError:
        jwt_claims = None
    except AttributeError:
        jwt_claims = None

    if jwt_claims is not None:
        username = jwt_get_username_from_claims(jwt_claims)
    else:
        username = None

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
        return None

    if not check_password(password, user.password):
        return None

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
        token = None
        claims = None

    return token, claims
