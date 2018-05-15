import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
from datetime import date, timedelta

from .models import Account, History, Rank


@asyncio.coroutine
async def parse_solved_questions(account, data):
    """
        Requesting every page asynchronously, and parsing every page with BeautifulSoup 4.

        Args:
            account: the cuurent account, Account
            data   : the dictionary of (account, solved questions), dict

    """
    async with aiohttp.ClientSession() as session:
        async with session.get(account.leetcode_url) as response:
            # check whether the request is successful
            if response.status == 200:
                soup = BeautifulSoup(await response.text(), "lxml")
                solved_question = soup.find_all(class_='badge progress-bar-success')[-5]
                data[account] = re.compile(r'\d+').findall(solved_question.string)[0]


def update_history_table(data):
    """
        Update the table of History.

        Args:
            data: the dictionary of (account, solved questions), dict

    """
    for account, solved_question in data.items():
        History.objects.create(
            solved_question=int(solved_question),
            date=date.today(),
            account=account
        )
    print('update History done.')


def update_rank_table():
    """
        Update the table of Rank.
    """
    rankings = []
    date_range = None
    # if Monday, date range is from yesterday to today 
    if date.today().weekday() == 0:
        date_range = (date.today() - timedelta(days=1), date.today())
    # otherwise, date range is from Monday of current week to today
    else:
        date_range = (date.today() - timedelta(days=date.today().weekday()), date.today())
    for account in Account.objects.all():
        history_set = account.history_set.filter(date__range=date_range)
        # at least two histories to get difference
        if history_set.count() > 1:
            # order by date
            history_set = history_set.order_by('date')
            # get difference between date range
            diff = history_set.last().solved_question - history_set.first().solved_question
            rankings.append((diff, account))
    # check whether there are new ranks to insert into the database 
    if len(rankings) > 0:
        # sort by diff, descending order 
        rankings.sort(key=lambda item: item[0], reverse=True)
        # previous difference
        prev_diff = 1000000
        # current ranking
        ranking = 1
        for i in range(0, len(rankings)):
            if rankings[i][0] < prev_diff:
                ranking = i + 1
                prev_diff = rankings[i][0]
            Rank.objects.create(ranking=ranking, date=date.today(), account=rankings[i][1])
        print('update Rank done.')
    else:
        print('no update of Rank')


def update_database():
    """
        Update the whole database. (Crontab Program)
    """
    # the dict to store the asynchronous result of requesting
    data = {}
    # all accounts
    accounts = Account.objects.all()
    # requesting
    tasks = [parse_solved_questions(account, data) for account in accounts]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    # check whether all pages are requested successfully
    if len(accounts) == len(data):
        # update the table of History
        update_history_table(data)
        # update the table of Rank
        update_rank_table()
        print('all update done.', date.today())
    else:
        print('requesting error', date.today())
