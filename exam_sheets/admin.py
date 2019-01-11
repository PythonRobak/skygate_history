from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm


from exam_sheets.models import ExamSheet, CompletedExaminationSheet

admin.site.register(ExamSheet)
admin.site.register(CompletedExaminationSheet)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['is_student', 'is_teacher',]


admin.site.register(User, UserAdmin)
