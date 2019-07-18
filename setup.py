import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_entur_monitor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL',
    description='Show departures from entur',
    long_description=README,
    url='https://github.com/datagutten/django-entur-monitor',
    author='Anders Birkenes',
    author_email='datagutten@datagutten.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ], install_requires=['django', 'dateutils', 'entur-api']
)
