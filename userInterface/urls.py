from django.urls import path
from . import views

urlpatterns = [
    path('analyst/<int:pk>', views.user_interface, name='user-interface'),
    path('rate/<int:pk>', views.rate_user_detail, name='user-rate'),
    path('oldcompany/<int:pk>', views.PervList, name='user-old-company'),
    path('rate/all', views.rateslist, name='all-user-rate'),
    path('analyst/all', views.analystslist, name='all-user-analyst'),
    path('home', views.user_home, name='user-home'),
    path('arrows/owned/all', views.CompanyArrowsAll, name='all-arrows-owned'),
    path('expects/all/recommened', views.expectList, name='all-user-expect'),
    path('real/all', views.expectrealList, name='real-user-expect'),
    path('company/<int:pk>', views.CapitalProfile, name='user-company'),
    path('research/<int:pk>', views.ResearchProfile, name='user-research'),
    path('expect/all', views.ExpectAll, name='all_expect'),

]
