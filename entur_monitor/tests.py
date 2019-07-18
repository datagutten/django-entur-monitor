from django.test import TestCase
from django.test.client import Client
from django.conf import settings


class MonitorTests(TestCase):
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
    )

    def setUp(self):
        self.client = Client()

        """settings.configure(
            DEBUG=True,
            # INSTALLED_APPS=self.INSTALLED_APPS + 'entur_monitor.apps.EnturMonitorConfig',
            DATABASE=None,
        )"""

    def test_monitor(self):
        response = self.client.get(
            '/monitor/NSR:StopPlace:58381/NSR:Quay:8027,NSR:Quay:8028/Majorstua%20(Tunnelbane)' +
            '/NSR:Quay:8050,NSR:Quay:8051/Majorstua%20(Sporvogn)?limit=15')
        self.assertEqual(response.status_code, 200)
