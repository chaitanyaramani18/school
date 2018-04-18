from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import loginview,logoutview, registerview,index
# from student.api.views import StudentDetail
from student.views import student_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),



    url(r'^login/', loginview, name='login'),
    url(r'^list/', student_view, name='student_view'),
    url(r'^$', index, name='index'),
    url(r'^register/', registerview, name='register'),
    url(r'^logout/', logoutview, name='logout'),
    url(r'^api/student/', include('student.api.urls')),
    # url(r'^?P<pk>\d+/$', StudentDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
