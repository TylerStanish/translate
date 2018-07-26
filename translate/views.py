from rest_framework.decorators import api_view
from rest_framework.response import Response

from translate.serializers import TranslateSerializer


@api_view(['GET', 'POST'])
def translation(request):
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        serializer = TranslateSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, 405)
        serializer.save()
        return Response(serializer.data, 201)
