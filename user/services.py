from django.db import IntegrityError

from auth.authentication import authenticate, generate_token
from auth.exceptions import AuthenticationError
from user.models import ThirdPartyLinks, User


def create_user(username, password):
    try:
        user = User.objects.create_user(username=username,
                                        password=password)
        if user is not None:
            ThirdPartyLinks.objects.create(user=user)
    except ValueError:
        raise
    except IntegrityError:
        raise

    return user


def authenticate_user(username, password):
    try:
        user = authenticate(username=username,
                            password=password)
        jwt, claims = generate_token(user)
    except AuthenticationError:
        raise

    return jwt, claims


def get_user_by_username(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None

    return user


def update_third_party_links(user,
                             leetcode_url=None,
                             github_url=None,
                             blog_url=None):
    if leetcode_url is not None:
        user.third_party_links.leetcode_url = leetcode_url
    if github_url is not None:
        user.third_party_links.github_url = github_url
    if blog_url is not None:
        user.third_party_links.blog_url = blog_url

    try:
        user.third_party_links.save()
    except ValueError:
        raise


def get_third_party_links_by_user(user):
    return user.third_party_links
