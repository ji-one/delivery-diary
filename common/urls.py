from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'common'

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', views.signin),
    path('api-token-auth/refresh/', views.refresh),
    path('update/info/', views.update_info),
    path('update/password/', views.update_password)
]
