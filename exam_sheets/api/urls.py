from .views import ExamSheetRudView

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ExamSheetRudView.as_view(), name='exam-sheet-rud')
]