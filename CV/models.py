from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class CV_Entry(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(default='')
    dateStart = models.DateField(default=timezone.now)
    dateEnd = models.DateField(default=timezone.now)


class Education(models.Model):
    facility = models.CharField(max_length=100)
    grades = models.TextField(default='')
    dateStart = models.DateField(default=timezone.now)
    dateEnd = models.DateField(default=timezone.now)


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
    name = models.CharField(max_length=100)
    dob = models.DateField(default=timezone.now)
    contactNumber = models.CharField(max_length=11)
