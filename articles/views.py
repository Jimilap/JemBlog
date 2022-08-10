from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . models import Article, Comment
from django.shortcuts import get_object_or_404

def index(request):
    articles_list = Article.objects.all()
    output = {'articles_list': articles_list}
    return render(request, 'list_of_articles.html', output)

def detail(request, article_id):
    
    article = Article.objects.get(id = article_id)
    try:
        comments = Comment.objects.filter(article = article_id)
    except Comment.DoesNotExist:
        comments = 0
    #publication date string
    pds = str(article.pub_date).replace('-', '.')
    #publication date array
    pda = (pds.split(':')[0] + ':' + pds.split(':')[1]).split(' ')
    output = {
        'title' : article.title,
        'text' : article.text,
        'author' : article.author,
        'pub_date' : "pub. date: " + pda[0] + " time: " + pda[1],
        'files' : article.files,
        'comments' : comments,
    }
    return render(request, 'article_page.html', output)

