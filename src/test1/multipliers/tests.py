# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase
from django.test import Client



class MyTestCase(TestCase):

    def setUp(self):

        self.client = Client()  # Каждому тесту нужен клиент.

    def detail(self):

        response = self.client.POST('') # Проверяет Пост запрос.
        self.assertEqual(response.status_code, 200) # Проверяет в ответе 200 код.