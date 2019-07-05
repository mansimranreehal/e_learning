from django.conf.urls import url
from frontpanel import views
app_name='frontpanel'
urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^verify_link/$', views.verify_link),
    url(r'^register/$', views.register),
    url(r'^admin_index/$', views.admin_index),
    url(r'^update_password/$', views.update_password),

]