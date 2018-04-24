from .views import StudentDetail, StudentList, StudentCreate
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='School API')
urlpatterns = [


    url(r'^(?P<pk>\d+)/$', StudentDetail.as_view()),
    url(r'^list/$', StudentList.as_view()),
    url(r'^create/$', StudentCreate.as_view()),
    url(r'^$', schema_view)


]