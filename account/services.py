from django.contrib.auth.models import User

from account.models import Account
from auth.authentication import authenticate, generate_token


def create_account(account_data):
    user = User.objects.create_user(username=account_data.username,
                                    password=account_data.password)
    Account.objects.create(
        leetcode_url=account_data.leetcode_url,
        github_url=account_data.github_url,
        blog_url=account_data.blog_url,
        user=user,
    )

    return user


def authenticate_account(username, password):
    user = authenticate(username=username,
                        password=password)
    if user is None:
        return None, None

    jwt, claims = generate_token(user)

    return jwt, claims
