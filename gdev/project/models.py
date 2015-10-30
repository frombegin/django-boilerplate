#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from ..common.abstract_models import TimestampedModel


class ProjectManager(models.Manager):
    pass


class Project(TimestampedModel):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    objects = ProjectManager()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Membership(models.Model):
    APPLYING = 0
    APPROVED = 1
    DENIED = 2

    STATUS_CHOICES = (
        (APPLYING, 'Applying'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)
    date_joined = models.DateField(auto_now_add=True)
    invite_reason = models.CharField(max_length=64)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
