from django.db import models

# Create your models here.
class Emp(models.Model):
    empid = models.CharField(max_length=100)
    empname = models.CharField(max_length=100)
    empemail = models.EmailField()
    empcontact = models.CharField(max_length=10)
    consultFees = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'emp'

class Patient(models.Model):
    patid = models.IntegerField(db_column='patid')
    patname = models.CharField(db_column='patname', max_length=100,blank=True, null=True)
    patge = models.IntegerField(db_column='patage')
    emp = models.ForeignKey(Emp, on_delete=models.CASCADE, default=0, blank=True)

    class Meta:
        db_table = 'patients'

class Genbill(models.Model):
    genlink = models.ForeignKey(Patient, on_delete=models.CASCADE,default=0)
    genid = models.IntegerField(null=True, blank=True)
    genname = models.CharField(max_length=100)
    genamt = models.DecimalField(max_digits=10, decimal_places=2)
    genamtpaid = models.DecimalField(max_digits=10, decimal_places=2)
    genamtdue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'bill'
