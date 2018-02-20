from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings


class DiveSiteList(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # views = models.IntegerField(default=0)
    # likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'DiveSiteList'

    def __str__(self):
        return self.name


class DiveSpot(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    rating = models.CharField(max_length=10)
    link = models.CharField(max_length=250)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class DiveClub(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.CharField(max_length=50, default='default')
    longitude = models.CharField(max_length=50, default='default')
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name