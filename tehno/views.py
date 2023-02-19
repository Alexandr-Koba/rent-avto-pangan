from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # поместил весь список в переменную
    return render(request, 'tehno/home.html', {'projects': projects}) # Возвращаем из запроса пользователя 