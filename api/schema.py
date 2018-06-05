import graphene

from api.mutation import Mutations
from api.query import Queries

schema = graphene.Schema(query=Queries, mutation=Mutations)
