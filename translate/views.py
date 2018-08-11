from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from google.cloud import translate_v2
import os
translate_client = translate_v2.Client()
translate_client = translate_client.from_service_account_json(os.path.abspath('./translate/TranslationAppCreds.json'))

from translate.serializers import (
    TranslateSerializerRequest,
    TranslateSerializerResponse,
    TranslateSerializerPatchRequest
)
from translate.models import TranslationEvent


@api_view(['GET', 'POST', 'PATCH'])
@permission_classes([IsAuthenticated,])
def translation(request):
    if request.method == 'GET':
        translations = TranslationEvent.objects.filter(user=request.user).order_by('-id')
        # translations = TranslationEvent.objects.all()
        serializer = TranslateSerializerResponse(translations, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer_request = TranslateSerializerRequest(data=request.data, context={'request': request})
        if not serializer_request.is_valid():
            return Response(serializer_request.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        translation_event = TranslationEvent(**serializer_request.data)
        translation_event.user = request.user
        translation_event.translation = translate_client.translate(
            values=translation_event.text,
            target_language=translation_event.to_lang,
            source_language=translation_event.from_lang
        )['translatedText']
        translation_event.save()

        serializer_response = TranslateSerializerResponse(translation_event)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)

    if request.method == 'PATCH':
        serializer_request = TranslateSerializerPatchRequest(data=request.data)
        if not serializer_request.is_valid():
            return Response(serializer_request.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        translation_event = TranslationEvent.objects.get(pk=serializer_request.data.get('id'))
        translation_event.will_practice = serializer_request.data.get('will_practice')
        translation_event.save()

        serializer_response = TranslateSerializerResponse(translation_event)
        return Response(serializer_response.data, status=status.HTTP_200_OK)
