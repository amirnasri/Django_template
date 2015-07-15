from django.shortcuts import render
from django.http import HttpResponse

def index(request, idx):
    context = {'idx': idx}
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'HelloWorldApp/template_index.html', context)
    
