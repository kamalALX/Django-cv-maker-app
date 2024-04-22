from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def cntc(request):
    return render(request, 'cntc.html', {})
