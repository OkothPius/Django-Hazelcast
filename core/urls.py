from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_map, name='list-map-objects'),
    path('create/', views.put_map, name='create-map'),
    path('queue/', views.get_queue, name='list-queue-objects'),
    path('queue-create/', views.put_queue, name='create-queue'),
    path('topic/', views.create_topic, name='get_topic'),

]
