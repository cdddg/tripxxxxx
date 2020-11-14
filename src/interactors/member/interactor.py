from orm import member, score

from ..base import BaseInteractor


class MemberInteractor(BaseInteractor):
    def get_member(self, id):
        return member.models.MemberBase.op.get(id=id)

    def get_members(self, input):
        return member.models.MemberBase.op.filter(**input.dict)

    def verify_member_favorite_tour_group(self, member_id, tour_group_id):
        return score.models.ScoreBaseLog.op.filter(member_id=member_id, tour_group_id=tour_group_id)
