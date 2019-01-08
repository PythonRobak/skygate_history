from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from exam_sheets.forms import CreateExamSheetAdminForm, CreateExamSheetTeacherForm
from exam_sheets.models import ExamSheet


class CreateExamSheet(View):



    def get(self, request):

        logged_user = request.user

        if logged_user.is_superuser == True:
            print("Zalogowany superuser")
            form = CreateExamSheetAdminForm()
            return render(request, 'create_exam_sheet.html', {'form': form})
        elif logged_user.is_teacher == True:
            print("Zalogowany nauczyciel")
            form = CreateExamSheetTeacherForm
            return render(request, 'create_exam_sheet.html', {'form': form})
        elif logged_user.is_student == True:
            print("Zalogowany student")
            return HttpResponse("You dont have permissions to create exam sheet")
        else:
            print("Zalogowany nie posiada żadnej roli")
            return HttpResponse("You dont have permissions to create exam sheet")

    def post(self, request):
        logged_user = request.user
        if logged_user.is_superuser == True:
            form = CreateExamSheetAdminForm(request.POST)
            if form.is_valid():
                return HttpResponse("Exam sheet archived")

        if logged_user.is_teacher == True:
            form = CreateExamSheetTeacherForm(request.POST)
            if form.is_valid():
                return HttpResponse("Exam sheet saved by teacher")

        # form = CreateExamSheetForm(request.POST)
        # if form.is_valid():
        #     if form.cleaned_data['password1'] != form.cleaned_data['password2']:
        #         msg = 'Password didnt match!'
        #         return render(request, 'webadminpanel/add-user.html', {'form': form, 'msg': msg})




            return redirect('users')

