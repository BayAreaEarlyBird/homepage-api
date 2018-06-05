from django.contrib.auth.models import User
from django.db import models


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
