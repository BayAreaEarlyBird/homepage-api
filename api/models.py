from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):

    leetcode_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200, null=True)
    blog_url = models.URLField(max_length=200, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.leetcode_url


class History(models.Model):

    solved_question = models.IntegerField()
    date = models.DateField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.user.username + ' ' + str(self.solved_question) + ' ' + \
            str(self.date.year) + ':' + str(self.date.month) + ':' + str(self.date.day)


class Rank(models.Model):

    ranking = models.IntegerField()
    diff = models.IntegerField()
    date = models.DateField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.user.username + ' ' + str(self.ranking) + ' ' + str(self.diff) + ' ' + \
            str(self.date.year) + ':' + str(self.date.month) + ':' + str(self.date.day)
