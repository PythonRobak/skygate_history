from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User


class CustomUser(AbstractBaseUser):


    is_student = models.BooleanField(
        _('student'),
        default=False,

    )
    is_teacher = models.BooleanField(
        _('teacher'),
        default=False,

    )

    def __str__(self):
        return self.username


class ExamSheet(models.Model):

    exam_sheet_title = models.CharField(max_length=50, blank=False)
    task_01_title = models.CharField(max_length=50, blank=False)
    task_01_description = models.TextField(blank=False)
    task_01_max_points = models.IntegerField(blank=False)

    task_02_title = models.CharField(max_length=50, blank=False)
    task_02_description = models.TextField(blank=False)
    task_02_max_points = models.IntegerField(blank=False)

    task_03_title = models.CharField(max_length=50, blank=False)
    task_03_description = models.TextField(blank=False)
    task_03_max_points = models.IntegerField(blank=False)

    task_04_title = models.CharField(max_length=50, blank=False)
    task_04_description = models.TextField(blank=False)
    task_04_max_points = models.IntegerField(blank=False)

    task_05_title = models.CharField(max_length=50, blank=False)
    task_05_description = models.TextField(blank=False)
    task_05_max_points = models.IntegerField(blank=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    archived = models.BooleanField(default=False)


class CompletedExaminationSheet(models.Model):

    completed_examination_sheet_title = models.CharField(max_length=50)
    task_01_title = models.CharField(max_length=50, blank=True, null=True)
    task_01_description = models.TextField()
    task_01_max_points = models.IntegerField(blank=True, default=0)
    answer_01 = models.TextField()
    answer_01_points_earned = models.IntegerField(blank=True, null=True)
    task_02_title = models.CharField(max_length=50, blank=True, null=True)
    task_02_description = models.TextField()
    task_02_max_points = models.IntegerField(blank=True, default=0)
    answer_02 = models.TextField()
    answer_02_points_earned = models.IntegerField(blank=True, null=True)
    task_03_title = models.CharField(max_length=50, blank=True, null=True)
    task_03_description = models.TextField()
    task_03_max_points = models.IntegerField(blank=True, default=0)
    answer_03 = models.TextField()
    answer_03_points_earned = models.IntegerField(blank=True, null=True)
    task_04_title = models.CharField(max_length=50, blank=True, null=True)
    task_04_description = models.TextField()
    task_04_max_points = models.IntegerField(blank=True, default=0)
    answer_04 = models.TextField()
    answer_04_points_earned = models.IntegerField(blank=True, null=True)
    task_05_title = models.CharField(max_length=50, blank=True, null=True)
    task_05_description = models.TextField()
    task_05_max_points = models.IntegerField(blank=True, default=0)
    answer_05 = models.TextField()
    answer_05_points_earned = models.IntegerField(blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    entrant = models.CharField(max_length=150, blank=True, null=True)
    final_rating = models.IntegerField(blank=True, null=True)

    checked = models.BooleanField(default=False)
    checked_by = models.CharField(max_length=150, blank=True, null=True)
    archived = models.BooleanField(default=False)















