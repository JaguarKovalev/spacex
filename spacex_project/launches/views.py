from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.shortcuts import render

def home(request):
    return render(request, 'launches/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('launches:login')
    else:
        form = UserCreationForm()
    return render(request, 'launches/register.html', {'form': form})
