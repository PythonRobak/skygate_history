from .views import ExamSheetRudView, ExamSheetAPIView, CompletedExaminationSheetAPIView

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', ExamSheetAPIView.as_view(), name='exam-sheet-create'),
    url(r'^(?P<pk>\d+)/$', ExamSheetRudView.as_view(), name='exam-sheet-rud'),
    url(r'^exam/$', CompletedExaminationSheetAPIView.as_view(), name='exam-sheet-create'),
    # url(r'^exam/(?P<pk>\d+)/$', ExamSheetRudView.as_view(), name='exam-sheet-rud'),
]