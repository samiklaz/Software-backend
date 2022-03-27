from django.test import TestCase, Client
from django.urls import reverse
from core.models import Cases
import json


class TestView(TestCase):
    def test_covid_api_GET(self):
        client = Client()
        response = client.get(reverse('core:covid_api', args=['Nigeria']))
        self.assertEqual(response.status_code, 200)