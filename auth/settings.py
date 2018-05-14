from django.conf import settings

USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

DEFAULTS = {

}
