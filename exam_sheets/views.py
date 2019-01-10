from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from exam_sheets.forms import CreateExamSheetAdminForm, CreateExamSheetTeacherForm
from exam_sheets.models import ExamSheet




class CreateExamSheet(View):



    def get(self, request):

        logged_user = request.user

        if logged_user.is_superuser == True:

            form = CreateExamSheetAdminForm()
            return render(request, 'create_exam_sheet.html', {'form': form})
        elif logged_user.is_teacher == True:

            form = CreateExamSheetTeacherForm
            return render(request, 'create_exam_sheet.html', {'form': form})
        elif logged_user.is_student == True:

            return HttpResponse("You dont have permissions to create exam sheet")
        else:
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
                sheet_to_save = ExamSheet.objects.create(
                    exam_sheet_title=form.cleaned_data['exam_sheet_title'],
                    task_01_title=form.cleaned_data['task_01_title'],
                    task_01_description=form.cleaned_data['task_01_description'],
                    task_01_max_points=form.cleaned_data['task_01_max_points'],
                    task_02_title=form.cleaned_data['task_01_title'],
                    task_02_description=form.cleaned_data['task_01_description'],
                    task_02_max_points=form.cleaned_data['task_01_max_points'],
                    task_03_title=form.cleaned_data['task_01_title'],
                    task_03_description=form.cleaned_data['task_01_description'],
                    task_03_max_points=form.cleaned_data['task_01_max_points'],
                    task_04_title=form.cleaned_data['task_01_title'],
                    task_04_description=form.cleaned_data['task_01_description'],
                    task_04_max_points=form.cleaned_data['task_01_max_points'],
                    task_05_title=form.cleaned_data['task_01_title'],
                    task_05_description=form.cleaned_data['task_01_description'],
                    task_05_max_points=form.cleaned_data['task_01_max_points'],
                    author=logged_user


                )
                sheet_to_save.save()
                return HttpResponse("Exam sheet saved by teacher")

        # form = CreateExamSheetForm(request.POST)
        # if form.is_valid():
        #     if form.cleaned_data['password1'] != form.cleaned_data['password2']:
        #         msg = 'Password didnt match!'
        #         return render(request, 'webadminpanel/add-user.html', {'form': form, 'msg': msg})




            return redirect('users')

