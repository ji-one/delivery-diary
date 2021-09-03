from django.urls import path
from . import views

urlpatterns = [
    path('', views.post),
    path('contribution/', views.contribution),
    path('analysis/', views.get_analysis_result)
]
