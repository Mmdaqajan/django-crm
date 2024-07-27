from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('add_record/', views.add_customer_record, name='add_record'),
    path('delete_record/<int:pk>/', views.delete_customer_record, name='delete_record'),
    path('edit_record/<int:pk>/', views.edit_customer_record, name='edit_record'),
]

