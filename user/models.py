from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return 'User object: %s' % super.__str__()


class ThirdPartyLinks(models.Model):
    leetcode_url = models.URLField(max_length=200, null=True)
    github_url = models.URLField(max_length=200, null=True)
    blog_url = models.URLField(max_length=200, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='third_party_links')

    def __str__(self):
        return '%s %s' % (self.user.username, self.leetcode_url)
