from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} now you can login !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{"form":form})
