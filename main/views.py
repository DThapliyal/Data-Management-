from django.shortcuts import render, redirect
from .forms import StudentRegisteration, userlogin
from .models import Users 
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .forms import Sign_up
from django.contrib.auth import authenticate , login , logout
from django.contrib import auth
# Create your views here.


def addandshow(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = StudentRegisteration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['Name']
                em = fm.cleaned_data['Email']
                ct = fm.cleaned_data['City']
                dp = fm.cleaned_data['Department']
                reg = Users(Name=nm, Email=em, City=ct, Department=dp)
                reg.save()
                messages.success(request, 'Employe Info Submitted')
                fm = StudentRegisteration()
        else:
            fm = StudentRegisteration()
        stud = Users.objects.all().order_by('id')
        paginate = Paginator(stud, 10)
        page_number = request.GET.get('page')
        finalData = paginate.get_page(page_number)
        lastpage=finalData.paginator.num_pages
        return render(request, 'addandshow.html', {'form': fm, 'stu':finalData, 'totalPages':lastpage, 'totalpage':[n+1 for n in range(lastpage)]})
    else:
        return redirect('/')


def delete_data(request, id):
    if request.method == 'POST':
        pi = Users.objects.get(pk=id)
        pi.delete()
    return redirect('/add')


def update_data(request, id):
    if request.method == 'POST':
        pi = Users.objects.get(pk=id)
        fm = StudentRegisteration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/add')
    else:
        pi = Users.objects.get(pk=id)
        fm = StudentRegisteration(instance=pi)
    return render(request, 'updatestudent.html', {'form': fm})

def sign_up (request):
    if request.method == 'POST':
        fm=Sign_up(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Employe Registered')
            return redirect('/signup')
    else:
        fm=Sign_up()
    return render(request,'sign_up.html',{'form':fm})

def Login_page(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=userlogin(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/add')
        else:
            fm=userlogin()
        return render(request,'login.html',{'form':fm})
    else:
        return redirect('/add')

def profile(request):
    return render(request,'profile.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

