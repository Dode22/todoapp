from django.shortcuts import render

# Create your views here.

def index(request): # the index view
    return render(request, 'todolist/index.html')