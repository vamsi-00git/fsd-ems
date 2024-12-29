from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Employee
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import IntegrityError


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('employees:admin_employee_list')
        else:
            return render(request, 'employees/login.html', {'error': 'Invalid credentials or not an admin'})

    return render(request, 'employees/login.html')



def logout_view(request):
    logout(request)
    return redirect('employees:login')


@login_required
def admin_employee_list_view(request):
    if not request.user.is_superuser:
        return redirect('employees:login')

    search_query = request.GET.get('search', '')
    if search_query:
        employees = Employee.objects.filter(name__icontains=search_query)
    else:
        employees = Employee.objects.all()

    total_count = employees.count()
    admin_username = request.user.username

    return render(request, 'employees/admin_employee_list.html', {
        'employees': employees,
        'total_count': total_count,
        'admin_username': admin_username,
        'search_query': search_query,
    })




@login_required
def edit_employee_view(request, employee_id):
    if not request.user.is_superuser:
        return redirect('employees:user_details')

    employee = get_object_or_404(Employee, id=employee_id)
    designation_choices = Employee.DESIGNATION_CHOICES

    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.mobile = request.POST['mobile']
        employee.designation = request.POST['designation']
        employee.gender = request.POST['gender']
        employee.courses = ", ".join(request.POST.getlist('courses'))
        if 'image' in request.FILES:
            employee.image = request.FILES['image']
        employee.save()
        return redirect('employees:admin_employee_list')

    return render(request, 'employees/edit_employee.html', {
        'employee': employee,
        'designation_choices': designation_choices,
    })

@login_required
def delete_employee_view(request, employee_id):
    if not request.user.is_superuser:
        return redirect('employees:user_details')

    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employees:admin_employee_list')


def register_employee_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        designation = request.POST['designation']
        gender = request.POST['gender']
        courses = ", ".join(request.POST.getlist('courses'))
        image = request.FILES.get('image')

        if Employee.objects.filter(email=email).exists():
            return render(request, 'employees/register_employee.html', {
                'error': 'An employee with this email already exists.'
            })

        try:
            Employee.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                designation=designation,
                gender=gender,
                courses=courses,
                image=image
            )
            return redirect('employees:admin_employee_list')

        except IntegrityError:
            return render(request, 'employees/register_employee.html', {
                'error': 'A unique constraint error occurred. Please try again.'
            })

    return render(request, 'employees/register_employee.html')







