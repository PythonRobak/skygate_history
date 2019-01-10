from django.contrib import admin
from exam_sheets.models import ExamSheet, CompletedExaminationSheet

admin.site.register(ExamSheet)
admin.site.register(CompletedExaminationSheet)
