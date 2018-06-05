from graphene import relay
from graphene_django import DjangoObjectType

from problem_solving.models import History, Rank


class HistoryType(DjangoObjectType):
    class Meta:
        model = History
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        return id


class RankType(DjangoObjectType):
    class Meta:
        model = Rank
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        return id
