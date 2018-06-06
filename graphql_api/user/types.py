from graphene import relay
from graphene_django import DjangoObjectType

import user.models


class ThirdPartyLinks(DjangoObjectType):
    """ The third-party links bound to the user."""

    class Meta:
        model = user.models.ThirdPartyLinks
        interfaces = (relay.Node,)
        description = 'The third-party links bound to the user.'

    @classmethod
    def get_node(cls, info, id):
        return id


class User(DjangoObjectType):
    """ A User object. """

    class Meta:
        model = user.models.User
        exclude_fields = ('password', 'is_superuser', 'is_staff')
        interfaces = (relay.Node,)
        description = 'A User object.'

    @classmethod
    def get_node(cls, info, id):
        return id
