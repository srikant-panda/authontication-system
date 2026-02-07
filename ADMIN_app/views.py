from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.views import debug
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# @csrf_exempt

def index(request):
    return render(request,'index.html')
def admin(request):
    if not request.session.get('admin_logged_in'):
        return redirect('/admin_login/')
    return render(request,'admin.html')



def admin_login(request):
    if request.method=='POST':
        print(request.POST)
        
        username=request.POST.get('username')
        password=request.POST.get('password')

        if (username=='admin' and password=='admin'):
            request.session['admin_logged_in']=True
            return redirect('/admin/')
        else:
            return render(request,'admin_login.html',{'ERROR':'Invalid Credentials'})
           
    
    return render(request , 'admin_login.html')
    




def admin_logout(request):
    
    request.session.flush()
    return render(request,'admin_logout.html')


# def page_505(request):
#     if HttpResponse("HTTP version not supported",statu=505)== 505:
#         return render(request , '505.html')