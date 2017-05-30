from setuptools import find_packages, setup

LONG_DESCRIPTION = """Django-Prometheus

This library contains code to expose some monitoring metrics relevant
to Django internals so they can be monitored by Prometheus.io.

See https://github.com/py-pa/django-prometheus for usage
instructions.
"""

setup(
    name="django-prometheus-py-pa",
    author="Thomas Frössman",
    author_email="thomasf@jossystem.se",
    description=(
        "Django middlewares to monitor your application with Prometheus.io."),
    license="Apache",
    keywords="django monitoring prometheus",
    url="http://github.com/py-pa/django-prometheus",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    test_suite="django_prometheus.tests",
    long_description=LONG_DESCRIPTION,
    install_requires=[
        "prometheus_client>=0.0.13",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Framework :: Django",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: Apache Software License",
    ],
)
