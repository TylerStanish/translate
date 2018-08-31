from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from translate.models import TranslationEvent
from translate.serializers import TranslateSerializerResponse


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def practice(request):
    if request.method == 'GET':
        practice_translations = TranslationEvent.objects.filter(will_practice=True, user=request.user)
        serializer = TranslateSerializerResponse(practice_translations, many=True)
        return Response(serializer.data)
