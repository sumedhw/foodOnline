from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from . forms import UserForm
from . models import User

# Create your views here.

def registerUser(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            
            # create user using form
            # password = form.changed_data['password']
            # user = form.save(commit=False)
            # user.role = User.CUSTOMER
            # user.set_password(password)
            # user.save()
            

            # create user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user  = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            print('User is created')

            messages.success(request, "Your account has been registered successfully!")

            return redirect('registerUser')
        else:
            print(form.errors)
            
            

    
    if request.method == 'GET':
        form = UserForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/registerUser.html',context=context)



def registerVendor(request):
    return render(request, 'accounts/registerVendor.html',context={})