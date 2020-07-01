from django.db import models


class CV_Entry(models.Model):
    title = models.TextField(default='')
    text = models.TextField(default='')
