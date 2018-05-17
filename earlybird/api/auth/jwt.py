import base64
from datetime import datetime, timedelta

from jose import jwt


def jwt_build_claim(user):
    """
        Build JWT claims for target user.

        Args:
              user: target user, User

        Returns:
              the claims of JWT, dict
    """
    claims = {
        'username': str(base64.b64encode(bytes(user.username, 'utf-8')), 'utf-8'),
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(days=10),
        'iss': 'EarlyBird'
    }
    return claims


def jwt_encode(claims):
    """
        Encode JWT claims into token.

        Args:
            claims: the claims of JWT, dict

        Return:
            encoded token, str
    """
    headers = {
        'alg': 'RS512',
        'typ': 'JWT'
    }
    with open('jwt_private_key.pem', 'r') as f:
        key = f.read()
    return jwt.encode(headers=headers, claims=claims, algorithm='RS512', key=key)


def jwt_decode(token):
    """
        Decode token into JWT claims and verify all of them.

        Args:
            token: the encoded token, str

        Return:
            the claims of JWT, dict

        Raises:
            jwt.JWTError: If the signature is invalid in any way.
            jwt.ExpiredSignatureError: If the signature has expired.
            jwt.ClaimsError: If any claim is invalid in any way.
    """
    with open('jwt_public_key.pem', 'r') as f:
        key = f.read()
    return jwt.decode(token=token, key=key)


def jwt_get_username_from_claims(claims):
    """
        Get username from target claims.

        Args:
            claims: target claims, dict

        Return:
            username for the target claims, str

    """
    username = claims.get('username')
    if username:
        return str(base64.urlsafe_b64decode(username), 'utf-8')
    return None


def jwt_get_token_from_info(info):
    """
        Get token from GraphQL resolver's info.

        Args:
            info: GraphQL resolver's info, dict

        Returns:
            encoded token, str
    """
    authorization = info.context.META.get('HTTP_AUTHORIZATION')
    if authorization:
        payload = authorization.split()
        try:
            token = payload[1]
            return token
        except IndexError:
            return None
    return None
