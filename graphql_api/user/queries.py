import graphene
from graphql import GraphQLError

from auth.decorators import extract_token
from graphql_api.user.types import User
from user.services import get_user_by_username


class Query(graphene.ObjectType):
    viewer = graphene.Field(User, description='The currently authenticated user.')
    user = graphene.Field(User,
                          username=graphene.String(required=True),
                          description='Lookup a user by username.')

    @staticmethod
    @extract_token
    def resolve_viewer(root, info, **kwargs):

        v = kwargs.get('viewer')
        if v is None:
            raise GraphQLError('Please log in.')
        return v

    @staticmethod
    def resolve_user(root, info, username, **kwargs):
        user = get_user_by_username(username=username)

        if user is None:
            raise GraphQLError('Cannot find user \'%s\'.' % username)

        return user
