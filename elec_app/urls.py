from django.conf.urls import url
from elec_app import views

urlpatterns = [
        url(r'^$', views.Home.as_view(), name="home"),
        url(r'^data$', views.HomeJson.as_view(), name="home_json")
]

