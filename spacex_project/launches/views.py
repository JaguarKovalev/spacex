from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.shortcuts import render
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import matplotlib.pyplot as plt
import os
from django.conf import settings

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'launches/login.html', {'form': form})

@login_required
def search_launches(request):
    year = request.GET.get('year', '')
    launches = []
    monthly_counts = [0] * 12  # Массив для подсчёта запусков по месяцам

    if year:
        url = "https://api.spacexdata.com/v4/launches"
        response = requests.get(url)
        if response.status_code == 200:
            all_launches = response.json()
            for launch in all_launches:
                if launch["date_utc"].startswith(year):
                    launches.append({
                        "mission_name": launch["name"],
                        "date": launch["date_utc"],
                        "success": launch["success"],
                        "rocket": launch["rocket"],
                    })
                    # Подсчёт запусков по месяцам
                    month = int(launch["date_utc"][5:7]) - 1
                    monthly_counts[month] += 1

            # Построение графика
            plt.bar(range(1, 13), monthly_counts)
            plt.title(f"Запуски SpaceX за {year}")
            plt.xlabel("Месяц")
            plt.ylabel("Количество запусков")
            plt.xticks(range(1, 13))
            # Сохранение графика в статическую папку
            graph_path = os.path.join(settings.MEDIA_ROOT, "launches_graph.png")
            plt.savefig(graph_path)
            plt.close()

    context = {
        "year": year,
        "launches": launches,
        "graph_url": "/media/launches_graph.png" if year else None,
    }
    return render(request, 'launches/search_results.html', context)


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

def about(request):
    return render(request, 'launches/about.html')
