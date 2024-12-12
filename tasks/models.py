from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()

    def get_detail_url(self):
        return reverse('tasks:detail', args = [self.pk])

    def get_update_url(self):
        return reverse('tasks:update', args = [self.pk])

    def get_delete_url(self):
        return reverse('tasks:delete', args=[self.pk])