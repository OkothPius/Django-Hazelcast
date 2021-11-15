from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_map, name='names'),
    path('create/', views.put_map, name='details'),
    path('queue/', views.get_queue, name='queue'),
    path('queue-create/', views.put_queue, name='queue-details'),
    path('topic/', views.create_topic, name='get_topic'),

]
