from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import *
from core.serializers import *
from core.urls import *


class TestUrls(SimpleTestCase):
    def test_covidApi_url_is_resolves(self):
        url = reverse('core:covid_api', args=['slug'])
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CovidAPIView)