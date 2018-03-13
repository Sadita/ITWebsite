from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings


class DiveSpot(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    link = models.CharField(max_length=250)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class DiveSite(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)
    description = models.CharField(max_length=1000, default="")
    image = models.CharField(max_length=1000, default="images/scotland.jpg")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DiveSite, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'DiveSiteList'

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

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username

