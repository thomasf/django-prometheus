# -*- coding: utf-8 -*-
import os
import subprocess
import sys

os.chdir('django_prometheus/tests/end2end')
sys.exit(subprocess.call('python manage.py test', shell=True))
