from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from . models import Article

def index(request):
    return render(request, 'list_of_articles.html')
    #return HttpResponse("Hello, world. You're at the polls index.")