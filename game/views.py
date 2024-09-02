from django.shortcuts import render, redirect
import random
from .models import List
import time
# Create your views here.
def first(request):
    return render(request, 'first.html')

def second(request):
    if List.objects.exists():
        lis = List.objects.get(id=1)
        lis.number1 = random.randint(1, 10)
        lis.number2 = random.randint(1, 10)
        lis.number3 = random.randint(1, 10)
    else:
        lis = List(id=1, number1=random.randint(1, 10), number2=random.randint(1, 10), number3=random.randint(1, 10))
    lis.save()
    return render(request, 'second.html', {
        'list': lis,
    })

def third(request):
    numbers = List.objects.get(id=1)
    condition = False
    message = ''
    if request.method == 'POST':
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        number3 = int(request.POST['number3'])
        print(number1, number2, number3)
        if number1 == numbers.number1 and number2 == numbers.number2 and number3 == numbers.number3:
            condition = True
            message = 'Congratulations! You have guessed the correct numbers.'
        else:
            message = 'Sorry! You have guessed the wrong numbers.'
    return render(request, 'third.html', {
        'condition': condition,
        'message': message,
    })
    