from django.urls import path
from . import views

urlpatterns = [
    path('add',views.addandshow, name='Add'),
    path('delete/<int:id>/',views.delete_data, name='Delete'),
    path('update/<int:id>/',views.update_data, name='Update'),
    path('signup',views.sign_up, name='Sign_up'),
    path('',views.Login_page, name='Login'),
    path('profile',views.profile, name='Profile'),
    path('logout',views.logout, name='Logout'),
]
