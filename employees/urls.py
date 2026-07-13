from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('view/<int:pk>/', views.view_employee, name='view_employee'),
    path('manage/<int:pk>/', views.manage_employee, name='manage_employee'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]