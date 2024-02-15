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



def campBossAddBus(request):
    context = {'success': False, 'error': None}  # Initialize context with success flag and error message
    
    if request.method == 'POST':
        number = request.POST.get('number')
        seats = request.POST.get('seats')
        
        # Check if the bus with this number already exists
        if Bus.objects.filter(BusNumber=number).exists():
            context['error'] = "Bus with this number already exists."
        else:
            bus = Bus(BusNumber=number, NumberOfSeats=seats)
            bus.save()
            context['success'] = True  # Set success to True after saving
    
    return render(request, './camp_app/campBossAddBus.html', context)



def campBossBase(request):
    return render(request,'./camp_app/campBossBase.html')


def AddItemCategory(request):
    return render(request,'./camp_app/campBossAddCategory.html')