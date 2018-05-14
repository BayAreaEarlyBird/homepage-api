from django.contrib.auth.backends import ModelBackend


class JWTBackend(ModelBackend):
    def authenticate(self, request, token=None, **kwargs):
        header = {}
        payload = {}
        key = read_file('')

        pass
