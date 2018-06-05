import datetime

import graphene

from account.services import create_account, authenticate_account
from api.account.types import AccountInput, TokenType, AuthenticationInput


class CreateAccount(graphene.Mutation):
    class Arguments:
        account_data = AccountInput(required=True)

    username = graphene.String()

    @staticmethod
    def mutate(root, info, account_data):
        user = create_account(account_data)
        return CreateAccount(username=user.username)


class CreateToken(graphene.Mutation):
    class Arguments:
        auth_data = AuthenticationInput(required=True)

    token = graphene.Field(TokenType)

    @staticmethod
    def mutate(root, info, auth_data=None):
        jwt, claims = authenticate_account(auth_data.username,
                                           auth_data.password)

        if jwt is not None and claims is not None:
            token = TokenType(token=jwt,
                              iat=datetime.datetime.fromtimestamp(claims.get('iat')),
                              exp=datetime.datetime.fromtimestamp(claims.get('exp')))
            return CreateToken(token=token)
        else:
            return None


class Mutation(graphene.ObjectType):
    create_account = CreateAccount.Field()
    create_token = CreateToken.Field()
