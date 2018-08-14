# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import OrForm

def or_view(request):
    check = []
    if request.method == 'POST': # Если это POST-запрос, то нам нужно обработать данные формы.
        form = OrForm(request.POST)
        if form.is_valid():   # Если форма валидна, то выполняем следующее.
            number = form.cleaned_data['result'] # Получение данных.
            for i in range(1, number + 1): # Пробегаем по циклу.
                if (number % i == 0): # Если число с формы делится на i без остатка, то выполняем следующее.
                    check.append(i)  # Добавляем i в check.
            return HttpResponse(' '.join(map(str,['Множители числа']+[form.cleaned_data['result']] +[':'] + check)))  # отправляем check c множителями и разбиваем по пробелам
    else:
        form = OrForm() # Если GET (или любой другой метод), то создаем пустую форму.

    return render(request, 'base.html', {'form': form})



