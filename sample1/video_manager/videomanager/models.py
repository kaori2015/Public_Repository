from django.db import models
from django.contrib.auth.models import AbstractUser

# videomanager/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        app_label = 'videomanager'


class CustomUser(AbstractUser):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ...
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set')
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    ...
    groups = models.ManyToManyField(Group, through='CustomUserGroup')
    user_permissions = models.ManyToManyField(Permission, through='CustomUserPermission')

class CustomUserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class CustomUserPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
