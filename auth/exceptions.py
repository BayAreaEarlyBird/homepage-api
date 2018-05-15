from django.core.exceptions import ValidationError


class AuthorizationFailed(ValidationError):
    """An error while authorizing the user."""
    pass
