
from . import views
from django.urls import path
from .views import camp_boss_add_category


urlpatterns = [
    path('', views.hrEmployeeLeaveStatus, name='hrEmployeeLeaveStatus'),
    path('campBossAddBus',views.campBossAddBus,name='campBossAddBus'),
    path('campBossBase',views.campBossBase,name='campBossBase'),
    path('camp/add-category/', camp_boss_add_category, name='camp_boss_add_category'),
]
