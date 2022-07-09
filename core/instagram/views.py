from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import Logins
from  .models import Register
# Create your views here.

def index(request):
    
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        Logins.objects.create(username=username, password=password).save()
        
        
        return redirect('mailindex')
    else:
        return render(request,'index.html')
    
def mailindex(request):
    if request.method == 'POST':
        email = request.POST['email2']
        password2 = request.POST['password2'] 
        Register.objects.create(email=email,password2=password2)
        
        return redirect('mailindex')
    else:
        return render(request,'mailindex.html')
     
        