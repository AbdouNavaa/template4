from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def projects(request):
    projects = Project.objects.all()
    if request.user.is_staff:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(Q(team__user__username=request.user))
        print('projs',projects)
    return render(request,'projects.html',{'projects':projects})

def courses(request):
    if request.user.is_staff:
        courses = Course.objects.all()
        return render(request,'courses.html',{'courses':courses})
        
    else:
        dev = Developper.objects.get(id=request.user.id -1)
        courses = Course.objects.filter(teacher=(request.user.id-1))
        return render(request,'courses.html',{'courses':courses,'dev':dev})
        
    # print('courses',courses[0].name)

from django.db.models import Q 
def files(request):
    if request.user.is_staff:
        files = File.objects.all()
    else:
        files = File.objects.filter(creater__user__username=request.user)
    pdfs = 0
    png = 0
    word = 0
    eps = 0
    for item in files:
        fs = item.name.split('.')
        if fs[1] == 'pdf':
            pdfs = pdfs + 1
        elif fs[1] == 'png':
            png += 1
        elif fs[1] == 'eps':
            eps += 1
        else:
            word +=1
        
    dev = Developper.objects.get(user= request.user)
    print('pdfs',pdfs)
    context = {'files':files,'pdfs':pdfs,'png':png,'eps':eps,'word':word,'dev':dev}
    return render(request,'files.html',context)

from django.contrib import messages
from .forms import *

def add_project(request):
    if request.method == 'POST':
        print('1')
        form = ProjectForm(request.POST, request.FILES)
        # print("Form",form['groupe'])
        if form.is_valid():
            print('2')
            form.save()
            print('3')
            messages.success(request, "Cours créé avec succès.")
            return redirect('template4:projects')  # Rediriger vers une liste des cours ou une autre page
        else:
            print('4')
            messages.error(request, "Erreur lors de la création du cours.")
    else:
        form = ProjectForm()
    
    return render(request, 'add_project.html', {'form': form})

def add_course(request, id):
    print('My_id',id) 
    dev = Developper.objects.get(id=id)
    if request.method == 'POST':
        print('1')
        form = CourseForm(request.POST, request.FILES)
        # print("Form",form['groupe'])
        if form.is_valid():
            print('2')
            cours_instance = form.save(commit=False)
            cours_instance.teacher = dev
            form.save()
            print('3')
            messages.success(request, "Cours créé avec succès.")
            return redirect('template4:courses')  # Rediriger vers une liste des cours ou une autre page
        else:
            print('4')
            messages.error(request, "Erreur lors de la création du cours.")
    else:
        form = CourseForm()
    
    return render(request, 'add_course.html', {'form': form,'dev': dev})

def add_skill(request,id):
    dev = Developper.objects.get(id=id)
    if request.method == 'POST':
        print('1')
        form = SkillForm(request.POST, request.FILES)
        # print("Form",form['groupe'])
        if form.is_valid():
            print('2')
            instance = form.save(commit=False)
            instance.dev = dev
            form.save()
            print('3')
            dev = Developper.objects.get(id=id)
            messages.success(request, "Cours créé avec succès.")
            return redirect('account:profile', dev)  # Rediriger vers une liste des cours ou une autre page
        else:
            print('4')
            messages.error(request, "Erreur lors de la création du cours.")
    else:
        form = SkillForm()
    return render(request,'add_skill.html',{'form':form,'dev':dev})    


def add_file(request,id):
    dev = Developper.objects.get(id=id)
    if request.method == 'POST':
        print('1')
        form = FileForm(request.POST, request.FILES)
        # print("Form",form['groupe'])
        if form.is_valid():
            print('2')
            instance = form.save(commit=False)
            instance.creater = dev
            form.save()
            print('3')
            messages.success(request, "Cours créé avec succès.")
            return redirect('account:profile', dev)  # Rediriger vers une liste des cours ou une autre page
        else:
            print('4')
            messages.error(request, "Erreur lors de la création du cours.")
    else:
        form = FileForm()
    return render(request,'add_file.html',{'form':form,'dev':dev})    

def add_activity(request, id):
    print('My_id',id) 
    dev = Developper.objects.get(id=id)
    if request.method == 'POST':
        print('1')
        form = ActivityForm(request.POST, request.FILES)
        # print("Form",form['groupe'])
        if form.is_valid():
            print('2')
            activity_instance = form.save(commit=False)
            activity_instance.user = dev
            form.save()
            print('3')
            dev = Developper.objects.get(id=id)
            messages.success(request, "Cours créé avec succès.")
            return redirect('account:profile', dev)  # Rediriger vers une liste des cours ou une autre page
        else:
            print('4')
            messages.error(request, "Erreur lors de la création du cours.")
    else:
        form = ActivityForm()
    return render(request,'add_activity.html',{'form':form,'dev':dev})    

def add_freind(request, id):
    print('My_id',id)
    dev = Developper.objects.get(id=id)
    
    # Récupérer ou créer l'objet Friend correspondant au développeur
    friend_obj, created = Friend.objects.get_or_create(user=dev)

    if request.method == 'POST':
        form = FreindForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Récupérer les amis à ajouter à partir du formulaire
            friends_to_add = form.cleaned_data['friends']
            print('1')
            # Vérifier si les amis sont déjà dans la liste
            existing_friends = friend_obj.friends.all()

            # Liste pour les amis ajoutés et ceux déjà existants
            new_friends = []
            already_friends = []

            for friend in friends_to_add:
                print('2')
                if friend in existing_friends:
                    already_friends.append(friend)
                    print('2')
                    
                else:
                    new_friends.append(friend)
                    print('21',new_friends)
                    
            
            if already_friends:
                messages.error(request, "Certains amis existent déjà dans la liste : " + ", ".join(str(f) for f in already_friends))

            if new_friends:
                # Ajouter les nouveaux amis à la liste
                print('3')
                
                friend_obj.friends.add(*new_friends)
                friend_obj.save()
                messages.success(request, "Amis ajoutés avec succès : " + ", ".join(str(f) for f in new_friends))
            
            print('31')
            return redirect('template4:freinds')  # Rediriger vers la liste des amis ou une autre page

        else:
            print('32')
            
            messages.error(request, "Erreur lors de l'ajout des amis.")
    
    else:
        form = FreindForm()
        print('4')
        

    return render(request, 'add_freind.html', {'form': form, 'dev': dev})


def freinds(request):
    freinds = Friend.objects.filter(Q(user__user__username=request.user))
    print('freinds1:',freinds)
    projects = Project.objects.all()
    # ).order_by('prof__user__username')
    print('usss:',request.user)
    dev = Developper.objects.get(user=request.user)
    return render(request,'freinds.html',{'freinds':freinds,'projects':projects,'dev':dev})

def delete_freind(request, id):
    freind = Friend.objects.get(id = id)
    freind.delete()
    return redirect('template4:freinds')