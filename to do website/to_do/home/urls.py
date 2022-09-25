from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('task/', views.task, name = 'task'),
    path('loginpage/', views.loginpage, name = 'loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('newtaskAdd/',views.newtaskAdd, name = 'newtaskAdd'),
    path('updatetask/<int:pk>',views.taskUpdate, name = 'updatetask'),
    path('deletetask/<int:pk>',views.taskDelete, name = 'deletetask'),
    

    
]

