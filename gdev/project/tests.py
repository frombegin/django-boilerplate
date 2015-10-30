#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from .models import ProjectManager, Project


class ModelTestCase(TestCase):
    def test_project_crud(self):
        self.assertEquals(0, Project.objects.count())
        project = Project.objects.create(name="testp")
        self.assertEquals("testp", project.name)
        self.assertEquals(1, Project.objects.count())
        Project.objects.all().delete()
        self.assertEquals(0, Project.objects.count())
