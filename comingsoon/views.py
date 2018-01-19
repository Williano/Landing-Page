from django.shortcuts import render


def home(request):
    context = {}
    template = 'comingsoon/home.html'
    return render(request, template, context)
