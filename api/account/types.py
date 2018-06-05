import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from account.models import Account


class UserType(DjangoObjectType):
    class Meta:
        model = User


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class AccountInput(graphene.InputObjectType):
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
