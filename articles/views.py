from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
#from . models import Article

def index(request):
    return render(request, 'front/list_of_articles.html')