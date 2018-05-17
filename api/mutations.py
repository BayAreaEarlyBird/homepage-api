import graphene
from django.contrib.auth.models import User

from api.models import Account
from api.types import AccountInput


class CreateAccount(graphene.Mutation):
    class Arguments:
        account_data = AccountInput(required=True)

    username = graphene.String()

    def mutate(self, info, account_data):
        user = User.objects.create_user(username=account_data.username,
                                        password=account_data.password)
        Account.objects.create(
            leetcode_url=account_data.leetcode_url,
            github_url=account_data.github_url,
            blog_url=account_data.blog_url,
            user=user,
        )
        return CreateAccount(username=user.username)


class Mutation(object):
    create_account = CreateAccount.Field()
