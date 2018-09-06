import graphene

from graphql_api.mutation import Mutations
from graphql_api.query import Queries

schema = graphene.Schema(query=Queries, mutation=Mutations)
