def get_leetcode_solved_number_records_on_date(user, date):
    return user.leetcodesolvednumberrecord_set.get(date)


def get_rank_records_on_date(user, date):
    return user.rankrecord_set.get(date)


def get_all_leetcode_solved_number_records(user):
    return user.rankrecord_set.all()


def get_all_rank_records(user):
    return user.rankrecord_set.all()
