from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from common.models import User
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from api.models import Diary


@api_view(['POST'])
def post(request):
    if not request.session.get('user_id'):
        return HttpResponse(status=401)
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    content = request.data.get('content')
    diary = Diary(user=user, title=request.data.get('title'), weather=request.data.get(
        'weather'), content=content, content_len=len(content))
    diary.save()
    return Response({'message': 'Written successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def contribution(request):
    if not request.session.get('user_id'):
        return HttpResponse(status=401)
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    diary = Diary.objects.filter(user=user).values('created_at', 'content_len')
    data = {}
    for item in diary:
        data[str(item['created_at'].timestamp())] = item['content_len']
    return JsonResponse(data, status=status.HTTP_200_OK)
