import graphene

from api.models import Account
from api.types import AccountType, HistoryType, RankType
from auth.decorators import token_required


class Query(object):
    account = graphene.Field(AccountType)
    history = graphene.Field(HistoryType, date=graphene.Date())
    rank = graphene.Field(RankType, date=graphene.Date())

    @token_required
    def resolve_account(self, info, **kwargs):
        user = kwargs.get('user')
        return Account.objects.get(user=user)

    @token_required
    def resolve_history(self, info, **kwargs):
        user = kwargs.get('user')
        return user.history_set.get(date=kwargs.get('date'))

    @token_required
    def resolve_rank(self, info, **kwargs):
        user = kwargs.get('user')
        return user.rank_set.filter(date=kwargs.get('date'))
