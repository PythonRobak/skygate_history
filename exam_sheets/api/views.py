from rest_framework import generics, mixins

from django.db.models import Q
from exam_sheets.models import ExamSheet
from .permissions import IsOwnerOrReadOnly
from .serializers import ExamSheetSerializer


# class ExamSheetListAPIView(generics.ListAPIView):
#     lookup_field = 'pk'
#     serializer_class = ExamSheetSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def get_queryset(self):
#         return ExamSheet.objects.all()


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
            print("case1 - title without ordering")
            # return qs

        if author is not None and order_by is None:
            qs = qs.filter(Q(author__username__icontains=author)).distinct()
            print("case2 - author without ordering")
            # return qs

        if title is not None and order_by is not None:
            qs = qs.filter(Q(exam_sheet_title__icontains=title)).order_by(order_by).distinct()
            print(f"case3 - title with ordering by {order_by}")
            # return qs

        if author is not None and order_by is not None:
            qs = qs.filter(Q(author__username__icontains=author)).order_by(order_by).distinct()
            print(f"case3 - author with ordering by{order_by}")
            # return qs

        # if title is not None and author is not None:
        #     qs = qs.filter(Q(exam_sheet_title__icontains=title)|Q(author__username__icontains=author)).distinct()
        #     print("case3 - title&author")
        #     return qs

        print(qs)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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