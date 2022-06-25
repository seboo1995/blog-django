from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('blog-home')
        else:
            messages.error(request,'ERROR in validating')
            return render(request, 'user/register.html',{'form':form})

    else:
        form = UserCreationForm()
        return render(request, 'user/register.html',{'form':form})