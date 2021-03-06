from django.db import models
from solo.models import SingletonModel


class EarningHeader(SingletonModel):
    first_header = models.CharField(max_length=255, null=True, blank=True)
    second_header = models.CharField(max_length=255, null=True, blank=True)
    third_header = models.CharField(max_length=255, null=True, blank=True)
    fourth_header = models.CharField(max_length=255, null=True, blank=True)
    fifth_header = models.CharField(max_length=255, null=True, blank=True)
    sixth_header = models.CharField(max_length=255, null=True, blank=True)
    seventh_header = models.CharField(max_length=255, null=True, blank=True)
    eight_header = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        pass


class EarningHeaderSecond(SingletonModel):
    first_header = models.CharField(max_length=255, null=True, blank=True)
    second_header = models.CharField(max_length=255, null=True, blank=True)
    third_header = models.CharField(max_length=255, null=True, blank=True)
    fourth_header = models.CharField(max_length=255, null=True, blank=True)
    fifth_header = models.CharField(max_length=255, null=True, blank=True)
    sixth_header = models.CharField(max_length=255, null=True, blank=True)
    seventh_header = models.CharField(max_length=255, null=True, blank=True)
    eight_header = models.CharField(max_length=255, null=True, blank=True)
    nine_header = models.CharField(max_length=255, null=True, blank=True)
    tenth_header = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        pass