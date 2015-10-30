#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class ProjectManager(models.Manager):
    pass


class Project(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    objects = ProjectManager()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    status = models.IntegerField(default=0)