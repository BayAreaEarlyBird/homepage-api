import graphene

from api.problem_solving.types import HistoryType, RankType
from auth.decorators import token_required
from problem_solving.services import get_history_on_date, get_rank_on_date


class Query(graphene.ObjectType):
    history = graphene.Field(HistoryType, date=graphene.Date())
    rank = graphene.Field(RankType, date=graphene.Date())

    @token_required
    def resolve_history(self, info, **kwargs):
        user = kwargs.get('user')
        date = kwargs.get('date')
        return get_history_on_date(user, date)

    @token_required
    def resolve_rank(self, info, **kwargs):
        user = kwargs.get('user')
        date = kwargs.get('date')
        return get_rank_on_date(user, date)
