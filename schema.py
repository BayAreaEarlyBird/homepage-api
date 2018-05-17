#!/usr/bin/env python
import graphene

import api.mutations
import api.queries
import auth.mutations


class Queries(api.queries.Query,
              graphene.ObjectType):
    pass


class Mutations(api.mutations.Mutation,
                auth.mutations.Mutation,
                graphene.ObjectType):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
