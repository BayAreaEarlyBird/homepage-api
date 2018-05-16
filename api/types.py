import graphene
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType

from api.models import Account, History, Rank


class UserType(DjangoObjectType):
    class Meta:
        model = User


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class HistoryType(DjangoObjectType):
    class Meta:
        model = History


class RankType(DjangoObjectType):
    class Meta:
        model = Rank


class AccountInput(graphene.InputObjectType):
    leetcode_url = graphene.String(required=True)
    github_url = graphene.String()
    blog_url = graphene.String()
    username = graphene.String(required=True)
    password = graphene.String(required=True)
