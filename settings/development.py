#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ._common import *

DEBUG = True
ALLOWED_HOSTS = []


DEBUG_APPS = (
    'debug_toolbar',
)

INSTALLED_APPS += DEBUG_APPS