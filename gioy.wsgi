# -*- coding: utf-8 -*-

import sys, os
import django.core.handlers.wsgi

sys.path.insert(0, '/home/proj/gioy')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = django.core.handlers.wsgi.WSGIHandler()
