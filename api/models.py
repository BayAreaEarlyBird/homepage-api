from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):

    current_weekly_rank = models.IntegerField()
    leetcode_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)
    blog_url = models.URLField(max_length=200)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Username: %s' % self.user.username


class WeeklyRank(models.Model):

    rank = models.IntegerField()
    date = models.DateField()

    user = models.ForeignKey(User, related_name="weekly_ranks", on_delete=models.CASCADE)

    def __str__(self):
        return 'His/Her weekly rank is %d' % self.rank
