from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory, APITestCase

from translate.views import translation


class TranslateTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='tystanish@gmail.com', password='strongpassword')

    def test_permission_translate_post(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/translate/')
        response = translation(request)
        self.assertEqual(response.status_code, 401)

    def test_permission_translate_get(self):
        pass
