import datetime

import graphene

from auth.authentication import authenticate, generate_token
from auth.types import AuthenticationInput, Token


class CreateToken(graphene.Mutation):
    class Arguments:
        auth_data = AuthenticationInput(required=True)

    token = graphene.Field(Token)

    @staticmethod
    def mutate(root, info, auth_data=None):
        user = authenticate(username=auth_data.username,
                            password=auth_data.password)
        if user is None:
            return None

        jwt, claims = generate_token(user)

        if jwt is not None and claims is not None:
            token = Token(token=jwt,
                          iat=datetime.datetime.fromtimestamp(claims.get('iat')),
                          exp=datetime.datetime.fromtimestamp(claims.get('exp')))
            return CreateToken(token=token)
        else:
            return CreateToken()


class Mutation(object):
    create_token = CreateToken.Field()
