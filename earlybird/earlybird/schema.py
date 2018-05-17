import graphene

import api.graphql.queries
import api.graphql.mutations


class Query(api.graphql.queries.Query, graphene.ObjectType):
    pass


class Mutation(api.graphql.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
