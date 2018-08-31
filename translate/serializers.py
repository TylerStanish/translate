from rest_framework import serializers

from google.cloud import translate

import os

translate_client = translate.Client()
translate_client = translate_client.from_service_account_json(os.path.abspath('./translate/TranslationAppCreds.json'))

from .models import TranslationEvent


class TranslateSerializerRequest(serializers.Serializer):

    from_lang = serializers.CharField(max_length=10)
    to_lang = serializers.CharField(max_length=10)
    text = serializers.CharField(max_length=1024)
    will_practice = serializers.BooleanField()


class TranslateSerializerResponse(serializers.ModelSerializer):

    class Meta:
        model = TranslationEvent
        exclude = ('user',)


class TranslateSerializerPatchRequest(serializers.Serializer):

    id = serializers.IntegerField()
    will_practice = serializers.BooleanField()
