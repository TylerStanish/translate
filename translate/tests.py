from collections import OrderedDict

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from translate.views import translation
from translate.models import TranslationEvent


class TranslateTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(email='tystanish@gmail.com', password='strongpassword')
        TranslationEvent.objects.create(
            id=1,
            from_lang='es',
            to_lang='en',
            text='¿esto es una broma?',
            translation='is this a joke?',
            will_practice=True,
            user=user
        )

    def test_POST_permission_translate_with_no_credentials(self):
        factory = APIRequestFactory()
        request = factory.post(reverse('translation'))
        response = translation(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_POST_permission_translate_with_credentials(self):
        # same as above but with a user
        factory = APIRequestFactory()
        user = User.objects.get(email='tystanish@gmail.com')
        request = factory.post(reverse('translation'), {
            'from_lang': 'en',
            'to_lang': 'es',
            'text': 'hello',
            'will_practice': True
        })
        force_authenticate(request, user)
        response = translation(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(TranslationEvent.objects.all()), 2)

    def test_GET_permission_translate_with_no_credentials(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('translation'))
        response = translation(request=request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_GET_permission_translate_with_credentials(self):
        factory = APIRequestFactory()
        user = User.objects.get(email='tystanish@gmail.com')
        request = factory.get(reverse('translation'))
        force_authenticate(request, user)
        response = translation(request=request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PATCH_will_practice_field(self):
        factory = APIRequestFactory()
        user = User.objects.get(email='tystanish@gmail.com')
        request = factory.patch(reverse('translation'), data={
            'id': TranslationEvent.objects.first().id,
            'will_practice': False
        })
        force_authenticate(request, user)
        response = translation(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(dict(response.data), dict(
            id=1,
            to_lang='en',
            from_lang='es',
            text='¿esto es una broma?',
            translation='is this a joke?',
            will_practice=False
        ))
