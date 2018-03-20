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
        self.rating = round(self.my_float, 2)
        super(DiveSite, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Divesites'

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


class Review(models.Model):
    divesite = models.ForeignKey(DiveSite)
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000, default="")
    date = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.rating)


class FutureDive(models.Model):
    user = models.ForeignKey(User)
    divesite = models.ForeignKey(DiveSite)

    def __str__(self):
        return self.divesite.name



class Picture(models.Model):
    location = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    pic = models.FileField()

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return '/scot-dives/photo-gallery/'
        #return u'/photo-gallery/'
        #return reverse('photogallery')
        #def get_absolute_url(self):

