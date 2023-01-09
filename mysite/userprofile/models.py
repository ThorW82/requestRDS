# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Role(models.TextChoices):
    DIRECTOR = 'DIRECTOR', 'Директор'
    MANAGER = 'MANAGER', 'Керівник відділу'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=None, blank=True, null=True,verbose_name='Роль')
    supervisor = models.ForeignKey("UserProfile", on_delete=models.CASCADE, verbose_name='Керівник', blank=True, default=None,
                                   null=True, related_name='supervisor_of')
    # can_view = models.ManyToManyField("UserProfile",  symmetrical = False, verbose_name='Бачуть заявки', blank=True, default=None)
    # avatar = models.ImageField(upload_to='images/users', verbose_name='Фото')

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


