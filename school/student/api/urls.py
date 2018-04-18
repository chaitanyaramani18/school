from .views import StudentDetail
from django.conf.urls import url
#
urlpatterns = [
#     # Examples:
#     # url(r'^$', 'school.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
      url(r'^(?P<pk>\d+)/$', StudentDetail.as_view())
    ]