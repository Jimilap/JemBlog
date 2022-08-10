from django.urls import path
from . import views
from . models import Article

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'), 
    path('<int:article_id>/', views.detail, name='detail'),
]
