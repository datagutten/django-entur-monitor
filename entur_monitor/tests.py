from django.test import SimpleTestCase
from django.test.client import Client
from django.conf import settings


class MonitorTests(SimpleTestCase):
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
    )

    def setUp(self):
        self.client = Client()

    def test_monitor(self):
        response = self.client.get(
            '/monitor/NSR:StopPlace:58381/NSR:Quay:8027,NSR:Quay:8028/Majorstua%20(Tunnelbane)' +
            '/NSR:Quay:8050,NSR:Quay:8051/Majorstua%20(Sporvogn)?limit=15')
        self.assertEqual(response.status_code, 200)

    def test_two_stops(self):
        response = self.client.get('/stops/NSR:StopPlace:4483/NSR:StopPlace:4478')
        self.assertContains(response, 'Majorstuen&nbsp;i Valkyriegata')
        self.assertContains(response, 'Majorstuen&nbsp;i Sørkedalsveien')
        self.assertContains(response, "url_left = '/refresh/NSR:StopPlace:4483?limit=20';")
        self.assertContains(response, "url_right = '/refresh/NSR:StopPlace:4478?limit=20';")

    def test_quays_with_name(self):
        response = self.client.get('/monitor/NSR:StopPlace:58381/NSR:Quay:8027,NSR:Quay:8028/Majorstua%20(Tunnelbane)/NSR:Quay:8050,NSR:Quay:8051/Majorstua%20(Sporvogn)?limit=15')
        self.assertContains(response, 'Majorstua (Tunnelbane)')
        self.assertContains(response, 'Majorstua (Sporvogn)')
        self.assertContains(response, "url_left = '/refresh/NSR:StopPlace:58381/NSR:Quay:8027,NSR:Quay:8028?limit=15';")
        self.assertContains(response, "url_right = '/refresh/NSR:StopPlace:58381/NSR:Quay:8050,NSR:Quay:8051?limit=15';")

    def test_refresh_stop(self):
        response = self.client.get('/refresh/NSR:StopPlace:4483?limit=20')
        self.assertContains(response, 'Ullerntoppen')

    def test_refresh_quays(self):
        response = self.client.get('/refresh/NSR:StopPlace:58381/NSR:Quay:8027,NSR:Quay:8028?limit=15')
        self.assertContains(response, 'Frognerseteren')