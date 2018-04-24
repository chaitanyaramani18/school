from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from student.models import Student


def student_view(request):
    obj_list = Student.objects.all()
    paginator = Paginator(obj_list,1) #how many obj(student_list) we need per page
    page = request.GET.get('page') # we are taking page nummber by this function
    print page
    try:
        obj = paginator.page(page)

    except PageNotAnInteger :
        obj = paginator.page(1)
    except EmptyPage :
        obj  = paginator.page(paginator.num_pages)

    return render(request,'list.html',{'obj':obj })




