import graphene

from api.user.types import ThirdPartyLinkType
from auth.decorators import token_required
from user.models import ThirdPartyLink


class Query(graphene.ObjectType):
    third_party_link = graphene.Field(ThirdPartyLinkType)

    @token_required
    def resolve_third_party_link(self, info, **kwargs):
        user = kwargs.get('user')
        return ThirdPartyLink.objects.get(user=user)
