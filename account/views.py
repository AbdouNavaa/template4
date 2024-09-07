from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
# import openpyxl
from .models import *
from template4.models import *
from .forms import *
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files import File
from datetime import datetime
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
# from django.core.paginator import Paginator
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile_image = form.cleaned_data.get('profile_image')
            author = Developper.objects.create(user=user, image=profile_image)
            auth_login(request, user)
            return redirect('accounts:authors')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})




def login(request):
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        print('Form:' ,form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_staff:
                    next_url = request.POST.get('next', 'template4:courses')
                    print('1')
                    return redirect('template4:courses')
                else:
                    print('1')
                    return redirect('account:profile', user)
            else:
                print('Authentication failed')
        else:
            print('11')
            print(form.errors)
    else:
        print('12')
        form = LogInForm()
    print('222222')
    return render(request, 'registration/login.html', {'form': form, 'next': request.GET.get('next', '')})


def logout(request):
    auth_logout(request)
    return render(request, 'registration/login.html',{})


from django.db.models import Q 
def profile(request,user):
    user = User.objects.get(username=user)
    print('User',user)
    if user.is_staff:
        return redirect('template4:courses')
    else:
        developper = get_object_or_404(Developper, user=user)
        print('developper',developper)
        activities = Activity.objects.filter(user=developper.id)
        skills = Language.objects.filter(dev=developper.id)
        
        # context = {'user':user,'developper': developper,'skill':skills[0],
        #             'skills':skills, "job":job , "activities":activities}
        context = {'user':user,'developper': developper,'skills':skills,
            "activities":activities}
        return render(request,'accounts/profile.html',context)
        


def profile_edit(request):
    profile = Developper.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})



    