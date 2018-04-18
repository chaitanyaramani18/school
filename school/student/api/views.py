from rest_framework import generics

from student.api.serializers import StudentSerializer
from student.models import Student


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_fields = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# class StudentList(generics.)