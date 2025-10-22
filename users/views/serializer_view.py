from rest_framework.decorators import api_view
from rest_framework.response import Response
from UserSetUp.users import serializers


@api_view(['POST'])
def createUser(request):
    serializer = serializers.CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data)
    return Response(serializer.errors, status=400)