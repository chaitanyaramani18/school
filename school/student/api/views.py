from rest_framework import generics

from student.api.serializers import StudentSerializer
from student.models import Student


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_fields = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(generics.CreateAPIView):
    lookup_fields = 'pk'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

# in below function we giving ability to createApi into LIstApi view..instead of writing two diffrent class as we wrote above '''

# class StudentList(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
# two way we can add ability to create api in listapi view
#
# first is
#     def post(self,request, *args,**kwargs):
#         return somethig
#
# another way we can use mixin
# import mixin
# class StudentList(mixins.CreateModelMixin, generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#  def perform_create(self,serializer):
#         serializer.save(user=self.request.user)
#     def post(self,request, *args,**kwargs):
#         return self.create(request, *args,**kwargs)
# above function also true for put delete method ..for put use update instead of create and same as delete



