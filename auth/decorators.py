from functools import wraps

from auth.authentication import authenticate
from auth.exceptions import AuthenticationError
from auth.utils import jwt_get_token_from_info


def extract_token(func=None):
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
        try:
            token = jwt_get_token_from_info(info)
            user = authenticate(token=token)
        except AuthenticationError as e:
            # raise GraphQLError('Failed to authenticate. %s' % e)
            return func(cls, info, **kwargs)

        return func(cls, info, viewer=user, **kwargs)

    return _wrapped
