from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('gallery/<int:id>', views.gallery),
    path('addgallery/<int:id>', views.addgallery),
    path('deletegallery/<int:id>', views.deletegallery),

]
