#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from gdev.common import abstract_models


class EmailUser(abstract_models.AbstractEmailUser):
    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    class Meta(abstract_models.AbstractEmailUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Profile(models.Model):
    user = models.OneToOneField(EmailUser)
    avatar = models.ImageField()
