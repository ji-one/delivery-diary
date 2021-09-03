from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from common.models import User
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from api.models import Analysis, Diary
import os
import json
from config import settings
from konlpy.tag import Okt
import asyncio
from datetime import datetime
from dateutil.relativedelta import relativedelta


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

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(sentiment_analysis(content))
    # loop.close()

    sentiment_analysis(user, content)  # TODO 비동기로 처리하고 싶다

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


def morphological_analysis(content):
    okt = Okt()
    words = okt.morphs(content, norm=True, stem=True)
    return words


def sentiment_analysis(user, content):
    file_dir = os.path.join(settings.MEDIA_ROOT, 'json')
    file_name = 'SentiWord_info.json'  # TODO json 파일 개선 필요

    try:
        if os.path.isfile(os.path.join(file_dir, file_name)):
            with open(os.path.join(file_dir, file_name), encoding='utf-8-sig', mode='r') as f:
                words = morphological_analysis(content)
                data = json.load(f)
                very_positive = positive = neutral = negative = very_negative = 0
                for word in words:
                    for i in range(0, len(data)):
                        if data[i]['word'] == word:
                            polarity = data[i]['polarity']
                            if polarity == '2':
                                very_positive += 1
                            if polarity == '1':
                                positive += 1
                            if polarity == '0':
                                neutral += 1
                            if polarity == '-1':
                                negative += 1
                            if polarity == '-2':
                                very_negative += 1

        analysis = Analysis(user=user, very_positive=very_positive, positive=positive,
                            neutral=neutral, negative=negative, very_negative=very_negative)
        analysis.save()

    except OSError:
        pass


@api_view(['GET'])
def get_analysis_result(request):
    if not request.session.get('user_id'):
        return HttpResponse(status=401)
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)

    now = datetime.now()
    before_one_month = now - relativedelta(months=1)
    result = Analysis.objects.filter(user=user, created_at__range=[before_one_month, now]).values(
        'very_positive', 'positive', 'neutral', 'negative', 'very_negative')

    data = {'very_positive': 0, 'positive': 0,
            'neutral': 0, 'negative': 0, 'very_negative': 0}

    for item in result:
        data['very_positive'] += item['very_positive']
        data['positive'] += item['positive']
        data['neutral'] += item['neutral']
        data['negative'] += item['negative']
        data['very_negative'] += item['very_negative']

    print(data)
    return JsonResponse(data, status=status.HTTP_200_OK)
