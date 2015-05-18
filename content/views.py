from django.shortcuts import render
import models
from django.http import Http404
def index(request):
    return render(request, 'index.html')
def article_listings(request, category=''):
    if category != '':
        enteredType = '0'
        for innerTuple in models.Article.TYPE_CHOICES:
            if category.lower() == innerTuple[1]:
                enteredType = innerTuple[0]
                break;
        if enteredType == '0':
            raise Http404("Page not found")
        return  render(request, 'article_listings.html', {'category': category.capitalize(), 'articles': models.Article.objects.filter(type = enteredType)})
    else:
        raise Http404("Page not found")
    return  render(request, 'article_listings.html', {'category': category.capitalize()})
def all_article_listings(request):
    return render(request, 'article_listings.html', {'category': 'All Articles', 'articles':models.Article.objects.all()})
def article(request, artID):
    art = models.Article.objects.get(pk=int(artID))
    file = 'article.html'
    if len(str(art.background)) > 4:
        file = 'article_with_background.html'
    return render(request, file, {'article': art})