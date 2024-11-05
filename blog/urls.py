from . import views
from django.urls import path

#Add URL pattern
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]