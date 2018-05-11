#!/usr/bin/env python
import graphene

from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User

from api.models import Account, WeeklyRank


class UserType(DjangoObjectType):
    class Meta:
        model = User


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class WeeklyRankType(DjangoObjectType):
    class Meta:
        model = WeeklyRank


class Query(object):
    all_users = graphene.List(UserType)
    all_accounts = graphene.List(AccountType)
    all_weeklyranks = graphene.List(WeeklyRankType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_accounts(self, info, **kwargs):
        return Account.objects.all()

    def resolve_all_weeklyranks(self, info, **kwargs):
        return WeeklyRank.objects.all()