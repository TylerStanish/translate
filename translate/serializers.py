from rest_framework import serializers

from google.cloud import translate

import os

translate_client = translate.Client()
translate_client = translate_client.from_service_account_json(os.path.abspath('./translate/TranslationAppCreds.json'))

from .models import TranslationEvent


class TranslateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        te = TranslationEvent(**validated_data)

        te.user = self.context['request'].user

        # do translation before creation
        te.translation = translate_client.translate(values=te.text, target_language=te.to_lang)
        te.save()
        return te

    class Meta:
        model = TranslationEvent
        exclude = ('user',)
