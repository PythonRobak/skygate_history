from rest_framework import generics, mixins, status
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import filters
from django.contrib.auth.models import User

from django.db.models import Q
from exam_sheets.models import ExamSheet, CompletedExaminationSheet
from .permissions import IsOwnerOrReadOnly
from .serializers import ExamSheetSerializer, CompletedExaminationSheetSerializer, \
    CompletedExaminationSheetSerializerAdmin, CompletedExaminationSheetSerializerStudent, \
    CompletedExaminationSheetSerializerTeacher


class ExamSheetAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'

    serializer_class = ExamSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):

        qs = ExamSheet.objects.all()
        title = self.request.GET.get("title")
        author = self.request.GET.get("author")
        order_by = self.request.GET.get("order_by")

        if title is not None and order_by is None:
            qs = qs.filter(Q(exam_sheet_title__icontains=title)).distinct()
            # print("case1 - title without ordering")

        if author is not None and order_by is None:
            qs = qs.filter(Q(author__username__icontains=author)).distinct()
            # print("case2 - author without ordering")

        if title is not None and order_by is not None:
            qs = qs.filter(Q(exam_sheet_title__icontains=title)).order_by(order_by).distinct()
            # print(f"case3 - title with ordering by {order_by}")

        if author is not None and order_by is not None:
            qs = qs.filter(Q(author__username__icontains=author)).order_by(order_by).distinct()
            # print(f"case3 - author with ordering by{order_by}")

        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExamSheetRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'

    serializer_class = ExamSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ExamSheet.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CompletedExaminationSheetAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    queryset = CompletedExaminationSheet.objects.all()

    filter_fields = ('completed_examination_sheet_title', 'entrant',)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return CompletedExaminationSheetSerializerAdmin

        if self.request.user.is_teacher:
            return CompletedExaminationSheetSerializerTeacher

        if self.request.user.is_student:
            return CompletedExaminationSheetSerializerStudent

        return CompletedExaminationSheetSerializer


class CompletedExaminationSheetRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    http_method_names = ['get', 'put', 'delete']


    def delete(self, request, *args, **kwargs):

        if self.request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        if self.request.user.is_teacher:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if self.request.user.is_student:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return CompletedExaminationSheetSerializerAdmin

        if self.request.user.is_teacher:
            return CompletedExaminationSheetSerializerTeacher

        if self.request.user.is_student:
            return CompletedExaminationSheetSerializerStudent


    def get_queryset(self):
        return CompletedExaminationSheet.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}