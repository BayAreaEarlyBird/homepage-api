from graphene_django.types import DjangoObjectType

from problem_solving.models import History, Rank


class HistoryType(DjangoObjectType):
    class Meta:
        model = History


class RankType(DjangoObjectType):
    class Meta:
        model = Rank
