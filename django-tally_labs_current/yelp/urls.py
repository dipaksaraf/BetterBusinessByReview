<<<<<<< HEAD
﻿from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import getPosNegPhrases
from .views import index
=======
﻿# yelp/urls.py

from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import home
>>>>>>> origin/master
from .views import YelpYelpScrapingCreateView
from .views import YelpYelpScrapingDetailsView


urlpatterns = {
<<<<<<< HEAD
    path('<slug:business_id>', getPosNegPhrases, name='getPosNegPhrases'),
    url(r'^index/$', index, name='index'),
    url(r'^review/$', 
        YelpYelpScrapingCreateView.as_view(), name="create"),
    url(r'^review/(?P<pk>[0-9a-f-]+)/$',
        YelpYelpScrapingDetailsView.as_view(), name="details"),
    # path('<uuid:uuid>',
    #      YelpYelpScrapingDetailsView.as_view(), name="details"),
=======
    path('<slug:business_id>', home, name='home'),
    url(r'^review/$', YelpYelpScrapingCreateView.as_view(), name="create"),
    url(r'^review/(?P<pk>[0-9a-f-]+)/$',
        YelpYelpScrapingDetailsView.as_view(), name="details"),
>>>>>>> origin/master
}

urlpatterns = format_suffix_patterns(urlpatterns)