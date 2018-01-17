import json

from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from shorts.models import ShortURL


class ShortURLTestCase(TestCase):

    def test_main_page(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        title = 'Make a short URL!'
        input = 'input type="url"'
        self.assertContains(response, title)
        self.assertContains(response, input)

    def test_invalid_url(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('main_page'), {'url': 'sdfsdfsdf'})
        content = json.loads(response.content)
        self.assertIn('errors', content)
        self.assertIn('url', content['errors'])
        self.assertEqual(content['errors']['url'][0], "Enter a valid URL.")

    def test_add_url(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('main_page'), {'url': 'https://www.youtube.com/'})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('new', content)
        self.assertTrue(len(content['new']) != 0)
        self.assertIn('short', content)
        self.assertTrue(len(content['short']) >= settings.SHORT_LEN_MIN)

    def test_visited(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        url = 'https://www.youtube.com/'
        response = self.client.post(reverse('main_page'), {'url': url})
        self.assertEqual(response.status_code, 200)
        obj = ShortURL.objects.get(url=url)
        self.assertEqual(obj.visited, 0)
        response = self.client.get(reverse('short_url_redirect', kwargs={'slug': obj.short}))
        self.assertEqual(response.status_code, 302)
        obj = ShortURL.objects.get(url=url)
        self.assertEqual(obj.visited, 1)
        self.client.get(reverse('short_url_redirect', kwargs={'slug': obj.short}))
        self.client.get(reverse('short_url_redirect', kwargs={'slug': obj.short}))
        obj = ShortURL.objects.get(url=url)
        self.assertEqual(obj.visited, 3)

