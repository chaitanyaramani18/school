from django.shortcuts import render
from student.models import Student



def student_view(request):
    obj = Student.objects.all()
    return render(request,'list.html',{'obj': obj})



