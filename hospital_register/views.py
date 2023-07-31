from django.shortcuts import get_object_or_404, render
from .models import Emp, Patient, Genbill
from django.http import HttpResponse, HttpResponseNotAllowed
from decimal import Decimal
# Create your views here.

def index(request):
    return render(request, "index.html",{})

def empreg(request):
    st = Emp.objects.all()
    return render(request, "empreg.html", {'st':st})

def insertEmp(request):
    vid = request.POST.get('tid')
    vname = request.POST.get('tname')
    vemail = request.POST.get('temail')
    vcontact = request.POST.get('tcontact')
    vconsult = Decimal(request.POST.get('tconsult'))
    us = Emp(empid=vid, empname=vname, empemail=vemail, empcontact=vcontact, consultFees=vconsult)
    us.save()
    return render(request, 'index.html', {})

def patreg(request):
    st = Patient.objects.all()
    mt = Emp.objects.all()
    return render(request, "patient.html", {'st': st, 'mt':mt})

def insertPat(request):
    pid = request.POST.get('pid')
    pname = request.POST.get('pname')
    page = request.POST.get('page')
    emp_id = request.POST.get('emp_id')
    emp = Emp.objects.get(empid=emp_id)
    us = Patient(patid=pid, patname=pname, patge=page, emp_id=emp.id)
    us.save()
    return render(request, 'index.html', {})

def genbill(request):
    st = Patient.objects.all()
    mt = Emp.objects.all()
    gt = Genbill.objects.all()
    return render(request, "genbill.html", {'st':st, 'mt':mt, 'gt':gt})

def insertBill(request):
    #st = Patient.objects.all()
    #mt = Emp.objects.all()
    #gt = Genbill.objects.all()
    genid = request.POST.get('pat_id')
    patient = Patient.objects.get(patid=genid)
    genname = patient.patname
    charges = request.POST.get('othercharges')
    #emp = patient.emp
    genid = patient.patid
    genamt = patient.emp.consultFees + Decimal(charges)
    genamtpaid = 0
    genamtdue = genamt - genamtpaid
    genlink_id = patient.id
    bill = Genbill(genlink_id=genlink_id, genid=genid, genname=genname, genamt=genamt, genamtpaid=genamtpaid, genamtdue=genamtdue)
    bill.save()
    return render(request, 'index.html', {})

def delete(request):
    return render(request, "delete.html", {})

def delete_by_id(request):
    table = request.GET.get("table","")
    id = request.GET.get("tdelete", "")
    if table=="emp":
        Emp.objects.filter(empid = id).delete()
        return render(request, 'index.html', {})
    else:
        Patient.objects.filter(patid = id).delete()
        return render(request, "index.html", {})

def update(request, id):
    record = Genbill.objects.get(id=id)
    return render(request, "update.html", {'record':record})

def deletebill(request, id):
    Genbill.objects.get(id=id).delete()
    return render(request, "index.html", {})

def updatedetails(request, id):
    record = Genbill.objects.get(id=id)
   # record.genamtpaid = record.genamtpaid + Decimal(request.POST.get('uamtpaid'))
    record.genamtpaid = Decimal(request.POST.get('uamtpaid'))
    record.genamtdue = record.genamt - record.genamtpaid
    record.save()
    return render(request, 'index.html', {})

def appointment(request):
    mt = Patient.objects.all
    return render(request, "appointment.html", {'mt':mt})

