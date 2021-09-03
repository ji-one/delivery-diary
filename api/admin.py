from django.contrib import admin

from .models import Diary
from api.models import Analysis

admin.site.register(Diary)
admin.site.register(Analysis)
