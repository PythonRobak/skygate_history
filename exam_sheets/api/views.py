from rest_framework import generics

from exam_sheets.models import ExamSheet
from .permissions import IsOwnerOrReadOnly
from .serializers import ExamSheetSerializer



class ExamSheetRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ExamSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # queryset                = BlogPost.objects.all()

    def get_queryset(self):
        return ExamSheet.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}