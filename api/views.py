from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from common.models import User
# Create your views here.
from django.http import HttpResponse
from api.models import Diary

@api_view(['POST'])
def post(request):
    if not request.session.get('user_id'):
        return HttpResponse(status=401)
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    diary = Diary(user=user, title=request.data.get('title'), weather=request.data.get(
        'weather'), content=request.data.get('content'))
    diary.save()
    return HttpResponse(status=201)
