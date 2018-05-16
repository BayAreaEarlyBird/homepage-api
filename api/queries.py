import graphene
from django.contrib.auth.models import User

from api.models import Account
from api.types import AccountType, HistoryType, RankType
from auth.decorators import token_required


class Query(graphene.ObjectType):

    account = graphene.Field(AccountType, username=graphene.String())
    history = graphene.Field(HistoryType, username=graphene.String(), date=graphene.Date())
    rank = graphene.Field(RankType, username=graphene.String(), date=graphene.Date())

    @token_required
    def resolve_account(self, info, **kwargs):
        user = kwargs.get('user')
        return Account.objects.get(user=user)

    @token_required
    def resolve_history(self, info, **kwargs):
        users = User.objects.filter(username=kwargs['username'])
        if len(users) == 0:
            return None
        account = Account.objects.filter(user=users[0])[0]
        history_set = account.history_set.filter(date=kwargs['date'])
        if len(history_set) == 0:
            return None
        return history_set[0]

    @token_required
    def resolve_rank(self, info, **kwargs):
        users = User.objects.filter(username=kwargs['username'])
        if len(users) == 0:
            return None
        account = Account.objects.filter(user=users[0])[0]
        rank_set = account.rank_set.filter(date=kwargs['date'])
        if len(rank_set) == 0:
            return None
        return rank_set[0]