"""Django-Prometheus

https://github.com/korfuri/django-prometheus
"""


import django_prometheus.middleware  # side effect: create metric objects # noqa
import django_prometheus.models  # side effect: create metric objects # noqa

# Import pip_prometheus to export the pip metrics automatically.
try:
    import pip_prometheus  # noqa
except ImportError:
    # If people don't have pip, don't export anything.
    pass

default_app_config = 'django_prometheus.apps.DjangoPrometheusConfig'
