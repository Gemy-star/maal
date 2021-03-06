import datetime

from django.db import models
from accounts.models import User


class CompanyCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', ])
        ]

    def __str__(self):
        return str(self.name)


class FinicialCompany(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to='logos/')
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.SET_NULL, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    total_arrows = models.FloatField(null=True, blank=True)
    arrow_value = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'category', ])
        ]

    def __str__(self):
        return self.name


class CompanyCode(models.Model):
    code = models.CharField(null=True, max_length=255, blank=True)
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company', null=True,
                                blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['code', 'company', ])
        ]

    def __str__(self):
        return self.code


class ResearchCompany(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name


class FinicialAnalyst(models.Model):
    logo = models.ImageField(null=True, )
    name = models.CharField(max_length=255, null=True, blank=True)
    CurrentJob = models.CharField(max_length=255, null=True, blank=True)
    currentCompany = models.ForeignKey(ResearchCompany, related_name='currentCompany', null=True,
                                       on_delete=models.SET_NULL, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    tiwtterAccount = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Analysts"
        ordering = ["id", ]
        indexes = [
            models.Index(fields=['name', 'phone', 'tiwtterAccount', 'email'])
        ]

    def __str__(self):
        return self.name


class Rates(models.Model):
    RECOMDATION_CHOICES = (
        (1, '?????????? ??????????'),
        (2, '?????????? ??????????'),
        (3, '??????????'),

    )
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.SET_NULL, related_name='CompanyEntered',
                                       null=True, blank=True)
    ResearchCompany = models.ForeignKey(ResearchCompany, on_delete=models.SET_NULL, related_name='ResearchCompany',
                                        null=True, blank=True)
    AnalayticName = models.ForeignKey(FinicialAnalyst, on_delete=models.SET_NULL, related_name='AnalayticName',
                                      null=True, blank=True)
    Recommendation = models.SmallIntegerField(max_length=255, null=True, blank=True, choices=RECOMDATION_CHOICES)
    FairValue = models.FloatField(null=True, blank=True)
    CurrenncyValue = models.FloatField(null=True, blank=True)
    MarketValue = models.FloatField(null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    RecommendDate = models.DateField(null=True)
    report = models.FileField(upload_to='reportspdf/', null=True)
    is_recommended = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        indexes = [
            models.Index(fields=['FairValue', 'AnalayticName', 'CompanyEntered'])
        ]

    @property
    def fair_percentage(self):
        return (self.FairValue - self.CurrenncyValue) / (self.CurrenncyValue * 100)

    @property
    def market_percentage(self):
        return (self.MarketValue - self.FairValue) / (self.FairValue * 100)

    def __str__(self):
        return str(self.CompanyEntered)


class PerviousCompany(models.Model):
    job = models.CharField(max_length=255, null=True, blank=True, )
    analyst = models.ForeignKey(FinicialAnalyst, on_delete=models.CASCADE, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True, )

    class Meta:
        indexes = [
            models.Index(fields=['job', 'analyst', 'company'])
        ]

    def __str__(self):
        return self.analyst.name


def current_year():
    return datetime.date.today().year


class RateQuarter(models.Model):
    QURATARYEARS = [
        ('?????????? ??????????', '?????????? ??????????'),
        ('?????????? ????????????', '?????????? ????????????'),
        ('?????????? ????????????', '?????????? ????????????'),
        ('?????????? ????????????', '?????????? ????????????'),
    ]
    year = models.IntegerField(null=True, default=current_year, blank=True)
    quaratar = models.CharField(max_length=255, choices=QURATARYEARS, default='?????????? ??????????', blank=True)
    value = models.PositiveIntegerField(null=True, default=0, blank=True)
    deviation_range = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.quaratar


class EarningsForecast(models.Model):
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    analyst = models.ForeignKey(FinicialAnalyst, on_delete=models.CASCADE, blank=True, null=True)
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE,
                                       null=True, related_name='expects', blank=True)
    ResearchCompany = models.ForeignKey(ResearchCompany, on_delete=models.CASCADE,
                                        null=True, related_name='Researchexpects', blank=True)
    report = models.FileField(upload_to='reportspdf/', null=True, blank=True)
    is_recommended = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return str(self.CompanyEntered.name)

    class Meta:
        indexes = [
            models.Index(fields=['analyst'])
        ]


class ExpectationYear(models.Model):
    real_earn = models.FloatField(null=True, blank=True)
    expect_earn = models.FloatField(null=True, blank=True)
    quarter_now = models.FloatField(null=True, blank=True)
    quarter_past = models.FloatField(null=True, blank=True)
    year = models.ForeignKey(EarningsForecast, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='deviations')

    class Meta:
        pass

    @property
    def deviation_real_now(self):
        result = float(self.real_earn) - float(self.quarter_now)
        deviation = result / self.quarter_now
        return deviation

    @property
    def deviation_expect_now(self):
        result = float(self.expect_earn) - float(self.quarter_now)
        deviation = result / self.quarter_now
        return deviation

    @property
    def deviation_on_expect(self):
        result = float(self.real_earn) - float(self.expect_earn)
        deviation = result / self.real_earn
        return deviation

    @property
    def deviation_real_past(self):
        result = float(self.real_earn) - float(self.quarter_past)
        deviation = result / self.quarter_past
        return deviation

    @property
    def deviation_expect_past(self):
        result = float(self.expect_earn) - float(self.quarter_past)
        deviation = result / self.quarter_past
        return deviation
