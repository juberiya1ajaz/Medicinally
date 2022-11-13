from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import FileSystemStorage

@login_required
def index(request):
    blood = request_blood.objects.filter(requester=request.user)
    donation = donations.objects.filter(name = request.user)
    brequest = request_blood_public.objects.filter(requester = request.user)
    apntmnt = blood_donate.objects.filter(donor = request.user)
    context = {
        'blood':blood,
        'donation': donation,
        'brequest':brequest,
        'apts' : apntmnt
    }
    return render(request,'index.html',context=context)
@login_required


@login_required
def social_help(request):
    if request.method=='POST':
        fid = request.POST.get('formid')
        if(fid=='1' or fid ==1):
            data = request_blood()
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='media/blood_request')
            filename = fs.save(myfile.name, myfile)
            hid = request.POST.get('Hid')
            data.hid = blood_bank.objects.get(id = hid)
            data.prescription = filename
            data.requester = request.user
            data.unit = request.POST.get('quantity') 
            data.save()
            print(data)
            return redirect('dashboard')
        if(fid=='2' or fid ==2):
            data = donations()
            myfile = request.FILES['myfile2']
            fs = FileSystemStorage(location='media/donations')
            filename = fs.save(myfile.name, myfile)
            data.prescription = filename
            data.name = request.user
            data.ammount = request.POST.get('money') 
            data.disease = request.POST.get('disease') 
            data.save()
            print(data)
            return redirect('dashboard')
        if(fid=='3' or fid ==3):
            data = request_blood_public()
            myfile = request.FILES['myfile3']
            fs = FileSystemStorage(location='media/req_blood')
            filename = fs.save(myfile.name, myfile)
            data.pres = filename
            data.requester = request.user
            data.units = request.POST.get('units') 
            data.group = request.POST.get('bgroup') 
            data.save()
            print(data)
            return redirect('dashboard')
        if(fid=='4' or fid==4):
            hname = request.POST.get('hsname')
            bgroup = request.POST.get('bdgroup')
            date = request.POST.get('date')
            data = blood_donate()
            data.donor = request.user
            data.location = blood_bank.objects.filter(name = hname)[0]
            data.bgroup = bgroup
            data.date = date
            data.save()
            return redirect('dashboard')

    blood = blood_bank.objects.all()
    donation = donations.objects.all()
    brequest = request_blood_public.objects.all()
    context = {
        'blood':blood,
        'donation': donation,
        'brequest':brequest
    }
    return render(request, 'social-help.html',context=context)

def skinCancer(request):
    return render(request,'diagnose.html')

def donateData(request):
    return render(request ,'donateData.html')