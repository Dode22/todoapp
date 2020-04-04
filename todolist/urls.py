# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]

from django.conf.urls import url
from django.contrib import admin
from todolist.views import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="Todolist"),
]