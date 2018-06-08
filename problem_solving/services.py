from .models import RankRecord

def get_leetcode_solved_number_records_on_date(user, date):
    return user.leetcode_solved_number_records.get(date)


def get_rank_records_on_date(user, date):
    return user.rank_records.get(date)


def get_all_leetcode_solved_number_records_by_user(user):
    return user.leetcode_solved_number_records.all()


def get_all_rank_records_by_user(user):
    return user.rank_records.all()


def get_all_rank_records():
    return RankRecord.objects.all()
