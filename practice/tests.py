from collections import OrderedDict

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from practice.views import practice
from translate.models import TranslationEvent


class PracticeTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(email='tystanish@gmail.com', password='password')
        TranslationEvent.objects.create(
            user=user,
            from_lang='en',
            to_lang='es',
            text='hello',
            translation='hola',
            will_practice=True
        )

    def test_permissions_of_practice_unauthenticated(self):
        factory = APIRequestFactory()
        request = factory.get(reverse(viewname='practice'))
        response = practice(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieval_of_practice(self):
        factory = APIRequestFactory()
        request = factory.get(reverse(viewname='practice'))
        force_authenticate(request, user=User.objects.get(email='tystanish@gmail.com'))
        response = practice(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [OrderedDict(
            from_lang='en',
            to_lang='es',
            text='hello',
            translation='hola',
            will_practice=True
        )])
