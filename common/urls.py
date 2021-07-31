from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
     path('signup/', views.signup),
     path('api-token-auth/', obtain_jwt_token),
]
