from graphene import relay
from graphene_django import DjangoObjectType

import problem_solving.models


class LeetcodeSolvedNumberRecord(DjangoObjectType):
    class Meta:
        # name = 'leetcode_solved_number_record'
        model = problem_solving.models.LeetcodeSolvedNumberRecord
        interfaces = (relay.Node,)
        description = 'A list contains historical number records of solved ' \
                      'problems in leetcode.'

    @classmethod
    def get_node(cls, info, id):
        return id


class RankRecord(DjangoObjectType):
    class Meta:
        model = problem_solving.models.RankRecord
        interfaces = (relay.Node,)
        description = 'A list contains rank records of the user.'

    @classmethod
    def get_node(cls, info, id):
        return id
