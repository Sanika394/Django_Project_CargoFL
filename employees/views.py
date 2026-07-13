from django.shortcuts import render ,redirect , get_object_or_404
from .models import Employee
from .forms import EmployeeForm

#It shows list of employees in employee list page
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def view_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/view_employee.html', {'employee': employee})

#Will show employee list and add employee form in the same page
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_add.html', {'form': form})

# will manage employee details in the same page
def manage_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/manage_employee.html', {'form': form, 'employee': employee})

#It deletes the emplyee and redirects to employee list page
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')