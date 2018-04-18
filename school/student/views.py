from django.shortcuts import render





# Create your views here.
from student.models import Student
# from student.serializer import StudentSerializer


def student_view(request):
    obj = Student.objects.all()
    return render(request,'list.html',{'obj': obj})


# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


