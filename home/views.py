from django.shortcuts import render
from .models import contact
# Create your views here.
def index(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
  
        contactinfo = contact(fname = fname, lname = lname)
        contactinfo.save()


    return render(request, 'index.html')