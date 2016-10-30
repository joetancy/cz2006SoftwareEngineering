from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.listing.user_id, filename)

ROOM_TYPES = (
    ('2-Room Flexi', '2-Room Flexi'),
    ('3-Room', '3-Room'),
    ('4-Room', '4-Room'),
    ('5-Room', '5-Room'),
    ('3Gen', '3Gen'),
    ('Executive Flat', 'Executive Flat'),
)


class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    block = models.CharField(max_length=5)
    street = models.CharField(max_length=200)
    floor = models.PositiveIntegerField()
    unit = models.CharField(max_length=4)
    postalCode = models.PositiveIntegerField()
    roomType = models.CharField(
        max_length=15, choices=ROOM_TYPES, default='2-Room Flexi')
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(max_length=500)
    askingPrice = models.PositiveIntegerField()
    dateListed = models.TimeField(auto_now=False, auto_now_add=True)
    dateUpdate = models.TimeField(auto_now=True, auto_now_add=False)
    statusClosed = models.BooleanField()


class ListingPicture(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
