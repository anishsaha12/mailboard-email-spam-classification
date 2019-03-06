from django.shortcuts import render

# Create your views here.
def employee_log(request):
    return render(request, 'employee/employee_log.html', {})