from django.conf.urls import include, url
from django.contrib import admin
# from accounts.views import loginview,logoutview, registerview,index

#from student.views import student_view

urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls')),
    url(r'^api/student/', include('student.api.urls')),
    url(r'^', include('accounts.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
