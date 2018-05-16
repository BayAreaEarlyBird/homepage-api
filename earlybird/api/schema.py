import graphene
from graphene_django.types import DjangoObjectType

from django.contrib.auth.models import User
from .models import Account, History, Rank


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


class CreateAccount(graphene.Mutation):
    class Arguments:
        account_data = AccountInput(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, account_data):
        ok = True
        user = User.objects.create(username=account_data.username , password=account_data.password)
        Account.objects.create(
            leetcode_url=account_data.leetcode_url,
            github_url=account_data.github_url,
            blog_url=account_data.blog_url,
            user=user,
        )
        return CreateAccount(ok=ok)


class Query(graphene.ObjectType):

    account = graphene.Field(AccountType, username=graphene.String())
    history = graphene.Field(HistoryType, username=graphene.String(), date=graphene.Date())
    rank = graphene.Field(RankType, username=graphene.String(), date=graphene.Date())

    def resolve_account(self, info, **kwargs):
        users = User.objects.filter(username=kwargs['username'])
        if len(users) == 0:
            return None
        return Account.objects.filter(user=users[0])[0]

    def resolve_history(self, info, **kwargs):
        users = User.objects.filter(username=kwargs['username'])
        if len(users) == 0:
            return None
        account = Account.objects.filter(user=users[0])[0]
        history_set = account.history_set.filter(date=kwargs['date'])
        if len(history_set) == 0:
            return None
        return history_set[0]

    def resolve_rank(self, info, **kwargs):
        users = User.objects.filter(username=kwargs['username'])
        if len(users) == 0:
            return None
        account = Account.objects.filter(user=users[0])[0]
        rank_set = account.rank_set.filter(date=kwargs['date'])
        if len(rank_set) == 0:
            return None
        return rank_set[0]
