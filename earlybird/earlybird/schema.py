import graphene
import api.schema


class Query(api.schema.Query):
    pass


class Mutations(graphene.ObjectType):
    create_account = api.schema.CreateAccount.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
