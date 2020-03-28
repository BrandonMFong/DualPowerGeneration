from django.db import models

# Create your models here.


class organization(models.Model):
    org_name = models.CharField(max_length=40)


class eUnit(models.Model):
    org_id = models.ForeignKey('organization', on_delete=models.CASCADE)
    code_name = models.CharField(max_length=40)
    solar_power = models.FloatField()
    wind_power = models.FloatField()
    time_duration = models.DurationField()


class tempdb(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name
