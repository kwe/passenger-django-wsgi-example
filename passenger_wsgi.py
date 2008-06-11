import os, sys
sys.path.append('/Users/kwe/Sites')
os.environ['DJANGO_SETTINGS_MODULE'] = 'wally.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()