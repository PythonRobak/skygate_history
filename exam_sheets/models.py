from django.contrib.auth.models import User
from django.db import models





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
    answer_01 = models.TextField()
    answer_01_points_earned = models.IntegerField(blank=False)
    answer_02 = models.TextField()
    answer_02_points_earned = models.IntegerField(blank=False)
    answer_03 = models.TextField()
    answer_03_points_earned = models.IntegerField(blank=False)
    answer_04 = models.TextField()
    answer_04_points_earned = models.IntegerField(blank=False)
    answer_05 = models.TextField()
    answer_05_points_earned = models.IntegerField(blank=False)

    entrant = models.ForeignKey(User, on_delete=models.CASCADE)
    average_score = models.FloatField(blank=False)
    final_rating = models.IntegerField(blank=False)

    checked = models.BooleanField(default=False)
    checked_by = models.CharField(max_length=150, blank=False, null=True)
    archived = models.BooleanField(default=False)















