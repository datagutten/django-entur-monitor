=============
Entur monitor
=============

Entur monitor is a django app to show departures from entur

Quick start
-----------

1. Add "entur_monitor" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'entur_monitor',
    ]

2. Include the entur_monitor URLconf in your project urls.py like this::

    path('entur_monitor/', include('entur-monitor.urls')),

