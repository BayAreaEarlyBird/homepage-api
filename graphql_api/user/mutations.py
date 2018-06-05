import datetime

import graphene

from graphql_api.user.types import UserInput, TokenType, AuthenticationInput
from user.services import create_user, authenticate_user


class CreateUser(graphene.Mutation):
    class Arguments:
        account_data = UserInput(required=True)

    username = graphene.String()

    @staticmethod
    def mutate(root, info, account_data):
        user = create_user(account_data)
        return CreateUser(username=user.username)


class CreateToken(graphene.Mutation):
    class Arguments:
        auth_data = AuthenticationInput(required=True)

    token = graphene.Field(TokenType)

    @staticmethod
    def mutate(root, info, auth_data=None):
        jwt, claims = authenticate_user(auth_data.username,
                                        auth_data.password)

        if jwt is not None and claims is not None:
            token = TokenType(token=jwt,
                              iat=datetime.datetime.fromtimestamp(claims.get('iat')),
                              exp=datetime.datetime.fromtimestamp(claims.get('exp')))
            return CreateToken(token=token)
        else:
            return None


class Mutation(graphene.ObjectType):
    create_account = CreateUser.Field()
    create_token = CreateToken.Field()
