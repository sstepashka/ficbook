from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.title


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.title


class Fiction(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return u'%s' % self.title


class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    exist = UserProfile.objects.filter(user=instance)
    print exist
    if created and exist.count() == 0:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
