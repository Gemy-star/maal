import datetime

from django.shortcuts import render
from office.models import FinicialAnalyst, FinicialCompany, Rates


def home_page(request):
    return render(request, 'main/home.html')


def reports_page(request):
    return render(request, 'main/reports.html')


def user_page(request):
    return render(request, 'main/user-home.html')


def master_home(request):
    context = {
        "high_rated": Rates.objects.all().order_by('-RecommendDate')[:10],
        "analysts": FinicialAnalyst.objects.all().order_by('-name')[:10],
        "today": datetime.datetime.now().date(),
        "rates_count": Rates.objects.count(),
        "analysts__count": FinicialAnalyst.objects.count(),
        "companies_count": FinicialCompany.objects.count()
    }
    return render(request, 'main/master_home.html', context=context)
