#!/usr/bin/env python
import graphene

import api.schema
import auth.mutations


class Queries(api.schema.Query, graphene.ObjectType):
    pass


class Mutations(auth.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
