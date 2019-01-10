from django_filters import rest_framework as filters

from exam_sheets.models import CompletedExaminationSheet


class ExamSheetFilter(filters.FilterSet):
    # completed_examination_sheet_title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CompletedExaminationSheet


        fields = {
            'completed_examination_sheet_title': ['icontains'],
            'author': ['exact'],
            'final_rating': ['lte', 'gte',]}

