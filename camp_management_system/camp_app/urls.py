
from . import views
from django.urls import path

urlpatterns = [
    path('', views.hrEmployeeLeaveStatus, name='hrEmployeeLeaveStatus'),
    path('campBossAddBus',views.campBossAddBus,name='campBossAddBus'),
    path('campBossBase',views.campBossBase,name='campBossBase'),
    path('campBossAddCategory',views.AddItemCategory,name='campBossAddCategory'),
]
