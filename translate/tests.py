from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from translate.views import translation
from translate.models import TranslationEvent


class TranslateTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='tystanish@gmail.com', password='strongpassword')

    def test_permission_translate_post_with_no_credentials(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/translate/')
        response = translation(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_translate_post_with_credentials(self):
        # same as above but with a user
        factory = APIRequestFactory()
        user = User.objects.get(email='tystanish@gmail.com')
        request = factory.post('/api/v1/translate/', {
            'from_lang': 'en',
            'to_lang': 'es',
            'text': 'hello',
            'will_practice': True
        })
        force_authenticate(request=request, user=user)
        response = translation(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(TranslationEvent.objects.all()), 1)

    def test_permission_translate_get(self):
        factory = APIRequestFactory()
        user = User.objects.get(email='tystanish@gmail.com')
        request = factory.get('/api/v1/translate/')
        force_authenticate(request=request, user=user)
        response = translation(request=request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_translation(self):
        pass
