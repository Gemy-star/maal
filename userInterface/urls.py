from django.urls import path
from . import views

urlpatterns = [
    path('analyst/<int:pk>', views.user_interface, name='user-interface'),
    path('rate/<int:pk>', views.rate_user_detail, name='user-rate'),
    path('oldcompany/<int:pk>', views.PervList, name='user-old-company'),
    path('rate/all', views.rateslist, name='all-user-rate'),
    path('analyst/all', views.analystslist, name='all-user-analyst')

]