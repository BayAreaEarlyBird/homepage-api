import asyncio
import re
from datetime import date, timedelta

import aiohttp
import urllib3
from bs4 import BeautifulSoup

from ..models import Account, History, Rank


def parse_solved_question(html):
    """
        Parse solved question from target html page.

        Args:
            html: target html page, str

        Return:
            solved question, str
    """
    soup = BeautifulSoup(html, "lxml")
    solved_question = soup.find_all(class_='badge progress-bar-success')[-5]
    return re.compile(r'\d+').findall(solved_question.string)[0]


@asyncio.coroutine
async def task(account, data):
    """
        Requesting every page asynchronously, and parsing every page with BeautifulSoup 4.

        Args:
            account: the current account, Account
            data   : the dictionary of (account, solved questions), dict

    """
    async with aiohttp.ClientSession() as session:
        async with session.get(account.leetcode_url) as response:
            # check whether the request is successful
            if response.status == 200:
                # parse solved question from response
                data[account] = parse_solved_question(await response.text())


def get_new_data_asynchronously(accounts, data):
    """
        Get new data for every account asynchronously.

        Args:
            accounts: all accounts to get new data, QuerySet
            data    : the dictionary of (account, solved questions), dict
    """
    # requesting and parsing
    tasks = [task(account, data) for account in accounts]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))


def get_new_data_synchronously(accounts, data):
    """
        Get new data for every account synchronously.

        Args:
            accounts: all accounts to get new data, QuerySet
            data    : the dictionary of (account, solved questions), dict
    """
    # disable warnings for SSL
    urllib3.disable_warnings()
    # requesting and parsing
    for account in accounts:
        response = urllib3.PoolManager().request('GET', url=account.leetcode_url)
        data[account] = parse_solved_question(response.data)


def get_new_data():
    """
        Get new data for every account. Retry when asynchronous requesting has errors.

        Return:
            data: the dictionary of (account, solved questions), dict
    """
    # the dict to store the asynchronous result of requesting
    data = {}
    # all accounts
    accounts = Account.objects.all()
    # requesting asynchronously first
    get_new_data_asynchronously(accounts, data)
    # check whether all requests are successful
    if len(accounts) == len(data):
        return data
    # reset data
    data = {}
    # retry requesting synchronously
    get_new_data_synchronously(accounts, data)
    # check whether all requests are successful
    if len(accounts) == len(data):
        return data
    return None


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


def update_rank_table():
    """
        Update the table of Rank.
    """
    # the list to store the tuple of (diff, account)
    rankings = []
    # if Monday, date range is from yesterday to today
    if date.today().weekday() == 0:
        date_range = (date.today() - timedelta(days=1), date.today())
    # otherwise, date range is from Monday of current week to today
    else:
        date_range = (date.today() - timedelta(days=date.today().weekday()), date.today())
    for account in Account.objects.all():
        # get histories in the date range for current account
        history_set = account.history_set.filter(date__range=date_range)
        # at least two histories to get difference
        if history_set.count() > 1:
            # order by date
            history_set = history_set.order_by('date')
            # get difference in the date range
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
            Rank.objects.create(
                ranking=ranking, diff=rankings[i][0],
                date=date.today(), account=rankings[i][1]
            )
