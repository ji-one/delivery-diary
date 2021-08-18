from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from common.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
import jwt


@permission_classes([AllowAny])
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'ID has already existed.'}, status=status.HTTP_400_BAD_REQUEST)

    # if password != password_confirmation:
    #     return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        encoded_jwt = jwt.encode(
            {'username': user.username, 'nickname': user.nickname, 'profile_image': str(user.profile_image), 'birthday': user.birthday.strftime('%Y-%m-%d'), 'phone_number': user.phone_number, 'address': user.address}, 'SECRET', algorithm='HS256').decode('utf-8')
        response = JsonResponse({"token": str(encoded_jwt)})
        return response

    return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([AllowAny])
@api_view(['PATCH'])
def update_info(request):
    user = User.objects.get(username=request.data.get('username'))
    user.nickname = request.data.get('nickname')
    user.birthday = request.data.get('birthday')
    # user.profile_image = request.FILES['profile_image']
    user.phone_number = request.data.get('phone_number')
    user.address = request.data.get('address')
    user.save()
    return Response({'message': 'User info updated successfully'}, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
@api_view(['PATCH'])
def update_password(request):
    user = User.objects.get(username=request.data.get('username'))
    new_password = request.data.get('newPassword')
    password_confirmation = request.data.get('passwordConfirmation')

    # if new_password != password_confirmation:
    #     return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()
    return Response({'message': 'Password updated successfully'}, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
@api_view(['POST'])
def refresh(request):
    user = User.objects.get(username=request.data.get('username'))
    encoded_jwt = jwt.encode(
        {'username': user.username, 'nickname': user.nickname, 'profile_image': str(user.profile_image), 'birthday': user.birthday.strftime('%Y-%m-%d'), 'phone_number': user.phone_number, 'address': user.address}, 'SECRET', algorithm='HS256').decode('utf-8')
    response = JsonResponse({"token": str(encoded_jwt)})
    return response
