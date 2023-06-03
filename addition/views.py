from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def addition(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 + num2
    return render(request, 'result.html', {'result': result})
