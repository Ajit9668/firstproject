from django.shortcuts import render,redirect
from .models import ModuleInfo

def createview(request):
    if request.method=='GET':
        return render(request,'firstapp/create.html')
    else:
        ModuleInfo(
            Module_Name=request.POST['name'],
            Module_Image=request.POST['image'],
            Module_Link=request.POST['link'],
            Module_SeqNo=request.POST['sequence']).save()
        return redirect(dataview)

def dataview(request):
    data=ModuleInfo.objects.all()
    return render(request,'firstapp/data.html',{'data':data})

def updatingview(request,id):
    data=ModuleInfo.objects.get(id=id)
    return render(request,'firstapp/updatedata.html',{'data':data})

def updatedview(request,id):
    data=ModuleInfo.objects.get(id=id)
    data.Module_Name=request.POST['name']
    data.Module_Image=request.POST['image']
    data.Module_Link=request.POST['link']
    data.Module_SeqNo=request.POST['sequence']
    data.save()
    return redirect(dataview)

def deleteview(request,id):
    data=ModuleInfo.objects.get(id=id)
    data.delete()
    return redirect(dataview)
