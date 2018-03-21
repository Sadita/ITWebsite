from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings


# The divesite model to create individual dive sites.
# A dive site has a name,
# A rating (which is the average of the ratings submitted by the users),
# Latitude and longitude representing the location of the site,
# A short description of the dive site,
# And an image of the dive site.
class DiveSite(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)
    description = models.CharField(max_length=1000, default="")
    image = models.CharField(max_length=1000, default="images/scotland.jpg")

    # The slug field returns the unique slugified name of the divesite
    # The rating returns the average rating rounded up to two decimal places
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.rating = round(self.rating, 2)
        super(DiveSite, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Divesites'

    def __str__(self):
        return self.name


# The Diveclub model to create individual clubs
# A club has a name,
# A latitude and longitude representing the location of the club,
# An address and a telephone for contact info.
class DiveClub(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.CharField(max_length=50, default='default')
    longitude = models.CharField(max_length=50, default='default')
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# The UserProfile model uses django's User model
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


# Review model for saving the rating and comments on a divesite given by a user
# DiveSite is foreign key because one divesite can have many reviews
# User is foreign key because one user can submit many reviews
# The composite key of divesite and user will be unique
# Date field to save the date when the review was posted
class Review(models.Model):
    divesite = models.ForeignKey(DiveSite)
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000, default="")
    date = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.rating)


# The FutureDive model is for the list of future dive sites the user save
# on their profile (like favorites)
# DiveSite is foreign key because one user can add multiple divesites on the list
# The composite key of divesite and user will be unique
class FutureDive(models.Model):
    user = models.ForeignKey(User)
    divesite = models.ForeignKey(DiveSite)

    def __str__(self):
        return self.divesite.name


# A picture model for individual pictures for the photo gallery
# A picture has a location (Where the photo was taken)
# A description (Is written by the user)
# And a pic (the file of the photo)
class Picture(models.Model):
    location = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    pic = models.FileField()

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return '/scot-dives/photo-gallery/'

