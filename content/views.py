from django.shortcuts import render
import models
from django.http import Http404
from content import functions
CATEGORIES = models.ArticleCategory.objects.all() #For navigation

def index(request):
    return render(request, 'index.html')
def all_article_listings(request):
    return render(request, 'article_listings.html', {'CATEGORIES': CATEGORIES, 'category': 'All Articles', 'articles':models.Article.objects.all().sort_by("-date", "title")})
def article_listings(request, category=''):
    #If a category was entered...
    if category != '':
        articles = '' #initializing to use outside of try-catch

        #Select ArticleCategory corresponding to category entered and select
        #all articles under this category
        try:
            articles = models.ArticleCategory.get(title = category).article_set.all()
        #Category doesn't exist, so 404 Error
        except:
            raise Http404("Article Category not found.")
        #Otherwise, successful!
        return  render(request, 'article_listings.html', {'CATEGORIES': CATEGORIES, 'category': category.capitalize(), 'articles': articles})
    #Else return all articles
    return  all_article_listings(request)


def article(request, artID):

    #Retrieve appropriate article
    try:
        art = models.Article.objects.get(pk=int(artID))
    except:
        raise Http404("Article not found.")
    outFile = 'article.html'#Template to use

    #Insert a <p> tag between each line break
    contentStyled = functions.autoLineBreak(art.content)

    #If there is a background url, change the template
    if len(str(art.background)) > 4:
        outFile = 'article_with_background.html'

    return render(request, outFile, {'CATEGORIES': CATEGORIES,'article': art, 'content': contentStyled})