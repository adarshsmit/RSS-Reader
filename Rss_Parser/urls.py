from django.conf.urls import include, url
from django.contrib import admin
from Reader import views

urlpatterns = [
    # Examples:
    url(r'^$', views.parse, name='parse'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
