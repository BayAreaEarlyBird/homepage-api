import graphene
from django.contrib.auth.models import User
from graphene import relay
from graphene_django import DjangoObjectType

from user.models import ThirdPartyLink


class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        return id


class ThirdPartyLinkType(DjangoObjectType):
    class Meta:
        model = ThirdPartyLink
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        return id


class UserInput(graphene.InputObjectType):
    leetcode_url = graphene.String(required=True)
    github_url = graphene.String()
    blog_url = graphene.String()
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class TokenFields(object):
    token = graphene.String()
    iat = graphene.DateTime()
    exp = graphene.DateTime()


class AuthenticationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class TokenType(graphene.ObjectType, TokenFields):
    pass
