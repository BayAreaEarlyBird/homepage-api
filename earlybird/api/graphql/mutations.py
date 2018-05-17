from datetime import datetime

from django.contrib.auth.models import User

import graphene

from api.models import Account
from api.auth.auth import verify_password, generate_token
from .types import AccountInput, AuthInput, TokenType


class CreateAccount(graphene.Mutation):
    class Arguments:
        account_data = AccountInput(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, account_data):
        # check whether the user exists or not
        if len(User.objects.filter(username=account_data.username)) > 0:
            return CreateAccount(ok=False)
        # create user
        user = User.objects.create_user(username=account_data.username, password=account_data.password)
        # create account
        Account.objects.create(
            leetcode_url=account_data.leetcode_url,
            github_url=account_data.github_url,
            blog_url=account_data.blog_url,
            user=user,
        )
        return CreateAccount(ok=True)


class CreateToken(graphene.Mutation):
    class Arguments:
        auth_data = AuthInput(required=True)

    ok = graphene.Boolean()
    token = graphene.Field(TokenType)

    def mutate(self, info, auth_data):
        # check whether the password is correct or not
        if not verify_password(username=auth_data.username, password=auth_data.password):
            return CreateToken(ok=False)
        # get target user
        user = User.objects.get(username=auth_data.username)
        # generate token
        claims, token = generate_token(user)
        if claims and token:
            return CreateToken(ok=True, token=TokenType(
                token=token,
                iat=datetime.fromtimestamp(claims.get('iat')),
                exp=datetime.fromtimestamp(claims.get('exp'))
            ))
        return CreateToken(ok=False)


class Mutation:
    create_account = CreateAccount.Field()
    create_token = CreateToken.Field()
