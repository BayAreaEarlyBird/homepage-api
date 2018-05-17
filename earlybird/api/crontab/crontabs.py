from datetime import date

from .utils import get_new_data, update_history_table, update_rank_table


def update_database():
    """
        Update the whole database.
    """
    # get new data
    data = get_new_data()
    # check whether all pages are requested successfully
    if data is None:
        print('requesting error', date.today())
    else:
        # update the table of History
        update_history_table(data)
        # update the table of Rank
        update_rank_table()
        print('all update done.', date.today())
