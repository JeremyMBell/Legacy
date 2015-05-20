from django.shortcuts import render
import models
from django.http import Http404
from content import functions
CATEGORIES = models.ArticleCategory.objects.all() #For navigation
NUM_ARTICLES = models.Article.objects.all().count()
ARTICLES = models.Article.objects.filter(id__gte = (NUM_ARTICLES - 10))
def index(request):
    return render(request, 'index.html', {'CATEGORIES': CATEGORIES, 'ARTICLES': ARTICLES})
def all_article_listings(request):
    return render(request, 'article_listings.html', {'CATEGORIES': CATEGORIES, 'category': 'All Articles', 'articles':models.Article.objects.all().sort_by("-date", "title")})
def article_listings(request, category=''):
    #If a category was entered...
    if not (category == '' or category.lower() == 'all'):
        articles = [] #initializing to use outside of try-catch
        cat = models.ArticleCategory()
        #Select ArticleCategory corresponding to category entered and select
        #all articles under this category
        try:
            cat = models.ArticleCategory.objects.get(name__iexact = category)
            articles = cat.article_set.all().order_by("-date", "title")
        #Category doesn't exist, so 404 Error
        except:
            raise Http404("Article Category not found.")
        #Otherwise, successful!
        return  render(request, 'article_listings.html', {'CATEGORIES': CATEGORIES, 'category': cat, 'articles': articles})
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

    return render(request, outFile, {'CATEGORIES': CATEGORIES, 'ARTICLES': ARTICLES, 'article': art, 'content': contentStyled})

def search(request):
    #This algorithm probably is inefficient due to all the looping, but this will
    #work for now
    if request.GET:
        original = request.GET['q']#original string
        allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"#don't confuse articles // easy to split tags
        new = ''
        #Reformated for tags
        for letter in original:
            if letter in allowed:
                new += letter
            else:
                new += ' '
        tags = new.split(' ')
        articles = []#Articles to return
        for tag in tags:
            addingNew = models.Article.filter(content__icontains = tag)
            #No duplicate articles
            for article in addingNew:
                if article not in articles:
                    articles += article#add an article
        return render(request, 'search.html', {'CATEGORIES': CATEGORIES, 'articles': articles, 'q': original})
    return render(request, 'search.html', {'CATEGORIES': CATEGORIES})