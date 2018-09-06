from django.conf import settings

# TODO(WanMok): Add Settings loader

USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

DEFAULTS = {

}
