from django.contrib.auth.models import User
from django.db import models


class CV_Entry(models.Model):
    title = models.TextField(default='')
    text = models.TextField(default='')


class Education(models.Model):
    facility = models.TextField(default='')
    grades = models.TextField(default='')


class Singleton(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()  # Since only one item

    def save(self, *args, **kwargs):
        if not self.pk and PersonalDetails.objects.exists():
            return
        return super().save(*args, **kwargs)


class PersonalDetails(Singleton):
    name = models.TextField(default='')
    dob = models.DateField()
    contactNumber = models.CharField(max_length=11)
