from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    template_name = 'app/current_time.html'
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return render(request, template_name, context = {'msg': msg})


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    list_dir = os.listdir()
    result = []
    template_name = 'app/dir.html'
    for element in list_dir:
        new_element = '- ' + element
        result.append(new_element)
    return render(request, template_name, context = {'result': result})
