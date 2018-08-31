from collections import OrderedDict

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from practice.views import practice
from translate.models import TranslationEvent


class PracticeTests(APITestCase):

    longMessage = True

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

    def test_GET_permissions_of_practice_unauthenticated(self):
        factory = APIRequestFactory()
        request = factory.get(reverse(viewname='practice'))
        response = practice(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_GET_practice(self):
        self.client.force_login(User.objects.get(email='tystanish@gmail.com'))
        response = self.client.get(reverse(viewname='practice'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # So I'm not using the APIRequestFactory because the response.data is an OrderedDict.
        # I can't guarantee the correct order of the keys and I don't care about the order either.
        # I also can't just convert the response.data to a dict by dict(response.data) because response.data is
        # a list
        self.assertListEqual(response.data, [dict(
            id=1,
            from_lang='en',
            to_lang='es',
            text='hello',
            translation='hola',
            will_practice=True
        )])
