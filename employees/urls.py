from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register-employee/', views.register_employee_view, name='register_employee'),
    path('employee-list/', views.admin_employee_list_view, name='admin_employee_list'),
    path('edit-employee/<int:employee_id>/', views.edit_employee_view, name='edit_employee'),
    path('delete-employee/<int:employee_id>/', views.delete_employee_view, name='delete_employee'),
    path('', views.login_view, name='root'),
]
