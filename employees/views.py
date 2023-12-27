from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employees.models import Employee

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)