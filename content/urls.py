from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Legacy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'view/(?P<artID>[0-9]+)/$', 'content.views.article'),
    url(r'(?P<category>[A-Za-z]+)/$', 'content.views.article_listings'),

    #url(r'$', 'content.views.all_article_listings'),
)
