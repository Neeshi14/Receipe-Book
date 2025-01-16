from django.shortcuts import render,redirect
##from .models import *
from django.shortcuts import redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
##from django.contrib.auth.decorators import login_required

# Create your views here.    
                                       

##@login_required(url="/login/")
def receipes(request):
    if request.method == "POST":
        print(request.POST)
        data = request.POST

        if(data.get('Search_re')):
            receipe_name = data.get('Search_re')
            queryset = Receipe.objects.filter(receipe_name__icontains = receipe_name)
            context = {'receipes': queryset}
            return render(request, 'receipes.html', context)

        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image=request.FILES.get("receipe_image")
        

        print(f"Name: {receipe_name}")
        print(f"Description: {receipe_description}")
        print(f"Image: {receipe_image}")


        if not receipe_name:
            return render(request, 'receipes.html', {'error': 'Recipe name is required.'})

        if not receipe_description:
            return render(request, 'receipes.html', {'error': 'Recipe description is required.'})


        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image= receipe_image,
        )

        return redirect('/receipes/')

    queryset = Receipe.objects.all()  

    context = {'receipes' : queryset} 
    return render(request , 'receipes.html', context)



##@login_required(url = "/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        
        data = request.POST

        receipe_image=request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')    
        

    context = {'receipe': queryset}
    return render(request , 'update.html',context)


##@login_required(url = "/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')      

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Username invalid")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Password invalid")
            return redirect('/login/')
        
        else:
            login(request , user)
            return redirect('/receipes/')
            

    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def Register(request):

   
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username already exits")
            return redirect('/Register/')
    
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Username sucessfully created")


        return redirect('/Register/')


    return render(request , 'Register.html')








