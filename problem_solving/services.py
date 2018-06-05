def get_history_on_date(user, date):
    return user.history_set.get(date)


def get_rank_on_date(user, date):
    return user.rank_set.filter(date)
