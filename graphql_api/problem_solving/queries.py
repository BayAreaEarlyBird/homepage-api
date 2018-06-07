import graphene


class Query(graphene.ObjectType):
    # history = graphene.Field(LeetcodeSolvedNumberRecord, date=graphene.Date())
    # rank = graphene.Field(RankRecord, date=graphene.Date())
    #
    # @extract_token
    # def resolve_history(self, info, **kwargs):
    #     user = kwargs.get('user')
    #     date = kwargs.get('date')
    #     return get_history_on_date(user, date)
    #
    # @extract_token
    # def resolve_rank(self, info, **kwargs):
    #     user = kwargs.get('user')
    #     date = kwargs.get('date')
    #     return get_rank_on_date(user, date)
    pass
