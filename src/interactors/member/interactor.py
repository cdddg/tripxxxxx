from ..base import BaseInteractor

from orm import member, score


class MemberInteractor(BaseInteractor):
    def get_member(self, id):
        return member.models.MemberBase.op.get(id=id)

    def get_members(self, input):
        return member.models.MemberBase.op.filter(**input.dict)

    # def member_add_favorite(self, input):
    #     return member.models.MemberFavorite.create(**input.dict)
