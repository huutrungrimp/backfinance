from django.db import models
from accounts.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=True)
    dated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)