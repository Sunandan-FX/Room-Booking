from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import BookingForm
# Create your views here.

def home(request):
    form = BookingForm()

    if(request.method == "POST"):
        form = BookingForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("Complete")
    return render(request,'Order/Home.html',{'form':form})
