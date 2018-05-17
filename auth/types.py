import graphene


class TokenFields(object):
    token = graphene.String()
    iat = graphene.DateTime()
    exp = graphene.DateTime()


class AuthenticationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class TokenType(graphene.ObjectType, TokenFields):
    pass
