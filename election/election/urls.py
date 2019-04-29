from django.conf.urls import url
from election import views

app_label = 'election'

urlpatterns = [
        url(r'^$', views.Home.as_view(), name="home"),
        url(r'^data$', views.HomeJson.as_view(), name="home_json")
]

