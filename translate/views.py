from rest_framework.decorators import api_view
from rest_framework.response import Response

from google.cloud import translate_v2
import os
translate_client = translate_v2.Client()
translate_client = translate_client.from_service_account_json(os.path.abspath('./translate/TranslationAppCreds.json'))

from translate.serializers import TranslateSerializerRequest, TranslateSerializerResponse
from translate.models import TranslationEvent


@api_view(['GET', 'POST'])
def translation(request):
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        serializer_request = TranslateSerializerRequest(data=request.data, context={'request': request})
        if not serializer_request.is_valid():
            return Response(serializer_request.errors, 405)

        translation_event = TranslationEvent(**serializer_request.data)
        translation_event.user = request.user
        translation_event.translation = translate_client.translate(
            values=translation_event.text,
            target_language=translation_event.to_lang,
            source_language=translation_event.from_lang
        )['translatedText']
        translation_event.save()

        serializer_response = TranslateSerializerResponse(translation_event)
        return Response(serializer_response.data, 201)
