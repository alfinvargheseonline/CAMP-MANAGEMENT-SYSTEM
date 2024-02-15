from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import *

def hrEmployeeLeaveStatus(request):
    # Fetch all leave status records
    leave_statuses = LeaveStatusModel.objects.all()
    context={'leave_status':leave_statuses}

    # Render the template with leave status data
    return render(request, './camp_app/hrEmployeeLeaveStatus.html',context)