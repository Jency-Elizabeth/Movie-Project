
from django.urls import path
from . import views
app_name='movieapp'

urlpatterns = [

    path('',views.lab,name='lab'),
    path('movie/<int:movie_id>/',views.list,name='list'),
    path('add/',views.add_list,name='add_list'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]