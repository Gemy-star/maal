from django.urls import path
from . import views

urlpatterns = [
    path('rates/list', views.RatesList, name='rates-list'),
    path('company/list', views.Company_List, name='company-list'),
    path('rates/<int:pk>', views.RateDetails, name='rate-details'),
    path('category/<int:pk>', views.CategoryDetails, name='category-details'),
    path('analyst/<int:pk>', views.AnalystDetails, name='analyst-details'),
    path('company/<int:pk>', views.CompanyDetails, name='company-details'),
    path('rates/update/<int:pk>', views.UpdateRate, name='rate-update'),
    path('rates/add', views.AddRate, name='rate-add'),
    path('category/update/<int:pk>', views.EditCategory, name='category-update'),
    path('research/update/<int:pk>', views.EditResearch, name='research-update'),
    path('company/update/<int:pk>', views.EditCompany, name='company-update'),
    path('analyst/update/<int:pk>', views.UpdateAnalyst, name='analyst-update'),
    path('analyst/add', views.AddAnalyst, name='analyst-add'),
    path('company/add', views.AddCompany, name='company-add'),
    path('research/add', views.AddResearch, name='research-add'),
    path('category/add', views.AddCategory, name='category-add'),
    path('research/list', views.Research_List, name='research-list'),
    path('category/list', views.Category_List, name='category-list'),
    path('analayst/list', views.AnalystsList, name='analyst-list'),
    path('rates/report', views.RatesAllReport.as_view(), name='rates-report'),
    path('analysts/report', views.AnalystsAllReport.as_view(), name='analysts-report'),
    path('pervcompany/list/<int:pk>', views.PervCompanyList, name='pervcompany-list'),
    path('pervcompany/add/<int:pk>', views.addPervCompany, name='pervcompany-add'),
    path('expectations/list', views.ExpectationList, name='expectations-list'),
]
