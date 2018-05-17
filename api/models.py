from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):

    leetcode_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200, null=True)
    blog_url = models.URLField(max_length=200, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user.username, self.leetcode_url)


class History(models.Model):

    solved_question = models.IntegerField()
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %d %s' % (self.user.username,
                             self.solved_question,
                             self.date)


class Rank(models.Model):

    ranking = models.IntegerField()
    diff = models.IntegerField()
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %d %d %s' % (self.user.username,
                                self.ranking,
                                self.diff,
                                self.date)
