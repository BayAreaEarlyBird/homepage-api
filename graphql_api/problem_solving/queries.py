import graphene
from graphene import relay

from graphql_api.problem_solving.types import RankRecordListingsConnection
from problem_solving.services import get_all_rank_records


class Query(graphene.ObjectType):
    rank_record_listings = relay.ConnectionField(
        RankRecordListingsConnection,
        description='Look up Rank Record listings.'
    )

    @staticmethod
    def resolve_rank_record_listings(root, info, **kwargs):
        return get_all_rank_records()
