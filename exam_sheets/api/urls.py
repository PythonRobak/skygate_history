from .views import ExamSheetRudView, ExamSheetAPIView

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', ExamSheetAPIView.as_view(), name='exam-sheet-create'),
    # url(r'^list$', ExamSheetListAPIView.as_view(), name='exam-sheet-list'),
    url(r'^(?P<pk>\d+)/$', ExamSheetRudView.as_view(), name='exam-sheet-rud'),
]