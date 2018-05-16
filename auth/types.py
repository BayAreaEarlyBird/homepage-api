import graphene


class TokenFields(graphene.AbstractType):
    token = graphene.String()
    iat = graphene.DateTime()
    exp = graphene.DateTime()


class AuthenticationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class Token(graphene.ObjectType, TokenFields):
    pass
