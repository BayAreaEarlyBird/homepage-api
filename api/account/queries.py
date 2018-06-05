import graphene

from account.models import Account
from api.account.types import AccountType
from auth.decorators import token_required


class Query(graphene.ObjectType):
    account = graphene.Field(AccountType)

    @token_required
    def resolve_account(self, info, **kwargs):
        user = kwargs.get('user')
        return Account.objects.get(user=user)
