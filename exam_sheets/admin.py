from django.contrib import admin

# Register your models here.
from exam_sheets.models import ExamSheet, CompletedExaminationSheet

admin.site.register(ExamSheet)
admin.site.register(CompletedExaminationSheet)
