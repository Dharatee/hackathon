from django.conf.urls import include, url
from . import views

app_name = "company"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'logout/$', views.logout, name="logout"),
]
