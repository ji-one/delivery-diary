from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from common.models import User


@permission_classes([AllowAny])
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'ID has already existed.'}, status=status.HTTP_400_BAD_REQUEST)

    if password != password_confirmation:
        return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
