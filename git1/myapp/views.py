from django.shortcuts import render
from django.http import HttpResponse
from .forms import Studeform
# Create your views here.
def Student(request):
    if request.method == 'POST':
        data = Studeform(request.POST)
        if data.is_valid():
            nm = data.cleaned_data["name"]
            ag = data.cleaned_data["age"]
            return render(request,'about.html',{'name':nm,'age':ag})
    else:
        data = Studeform()
        return render(request,"home.html",{'data':data})