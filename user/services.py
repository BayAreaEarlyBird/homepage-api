from django.contrib.auth.models import User
from django.db import IntegrityError

from auth.authentication import authenticate, generate_token
from user.models import ThirdPartyLink


def create_user(account_data):
    try:
        user = User.objects.create_user(username=account_data.username,
                                        password=account_data.password)

        ThirdPartyLink.objects.create(
            leetcode_url=account_data.leetcode_url,
            github_url=account_data.github_url,
            blog_url=account_data.blog_url,
            user=user,
        )
    except ValueError:
        raise
    except IntegrityError:
        raise

    return user


def authenticate_user(username, password):
    user = authenticate(username=username,
                        password=password)
    if user is None:
        return None, None

    jwt, claims = generate_token(user)

    return jwt, claims
