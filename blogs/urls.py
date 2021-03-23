from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
]