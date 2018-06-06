from django.db import models

from user.models import User


class LeetcodeSolvedNumberRecord(models.Model):
    # class Meta:
    #     verbose_name = 'leetcode_solved_number_record'

    solved_question = models.IntegerField()
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='leetcode_solved_number_records')

    def __str__(self):
        return '%s %d %s' % (self.user.username,
                             self.solved_question,
                             self.date)


class RankRecord(models.Model):
    ranking = models.IntegerField()
    diff = models.IntegerField()
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='rank_records')

    def __str__(self):
        return '%s %d %d %s' % (self.user.username,
                                self.ranking,
                                self.diff,
                                self.date)
