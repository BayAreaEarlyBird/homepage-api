from functools import wraps

from auth.authentication import authenticate
from auth.utils import jwt_get_token_from_info


def token_required(func=None):
    """ Decorates the function to determine whether needs token.

    This decorator will add hydrated User object into the context that makes
    sure the business logic layer can receive the authenticated user.

    Args:
        func: A function in Graphene.

    Returns:
        _wrapped: A wrapped function.
    """

    @wraps(func)
    def _wrapped(cls, info, **kwargs):
        token = jwt_get_token_from_info(info)
        user = authenticate(token=token)
        if user:
            return func(cls, info, user=user, **kwargs)
        else:
            return None

    return _wrapped
