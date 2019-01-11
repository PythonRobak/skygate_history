from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import request

from exam_sheets.models import ExamSheet


class CreateExamSheetAdminForm(forms.ModelForm):

    class Meta:
        model = ExamSheet
        fields = [
            'exam_sheet_title',
            'archived'
        ]

class CreateExamSheetTeacherForm(forms.ModelForm):

    class Meta:
        model = ExamSheet
        fields = [
            'exam_sheet_title',
            'task_01_title',
            'task_01_description',
            'task_01_max_points',

            'task_02_title',
            'task_02_description',
            'task_02_max_points',

            'task_03_title',
            'task_03_description',
            'task_03_max_points',

            'task_04_title',
            'task_04_description',
            'task_04_max_points',

            'task_05_title',
            'task_05_description',
            'task_05_max_points'
        ]


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('is_student', 'is_teacher')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('is_student', 'is_teacher')