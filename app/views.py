from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_school(request):
    if request.method=="POST":
        scname=request.POST["scname"]
        sp=request.POST["scprincipal"]
        sloc=request.POST["sclocation"]

        so=school.objects.get_or_create(scname=scname,scprincipal=sp,sclocation=sloc)[0]
        so.save()

        qsso=school.objects.all()
        d={"qsso":qsso}
        return render(request,"display_school.html",d)
    return render(request,"insert_school.html")

def insert_student(request):
    if(request.method=="POST"):
        schoolname=request.POST["scname"]
        stname=request.POST["stn"]
        stid=request.POST["stid"]

        sobj=school.objects.get(scname=schoolname)
        studento=student.objects.get_or_create(scname=sobj,studentname=stname,sid=stid)[0]
        studento.save()

        qsstudent=student.objects.all()
        dict={"qsstudent":qsstudent}
        return render(request,"display_student.html",dict)
    return render(request,"insert_student.html")

