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

    def test_newest(self):
        import threading
        Project.objects.create(name="test1")
        threading._sleep(0.001)
        Project.objects.create(name="test2")
        threading._sleep(0.001)
        Project.objects.create(name="test3")
        newest = Project.objects.newest()[0]
        self.assertEquals('test3', newest.name)

    def test_popular(self):
        pass