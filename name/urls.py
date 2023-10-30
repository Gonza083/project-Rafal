"""name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ui_app import views

urlpatterns = [
    #path de ui_app
    path('', views.home, name="home"),
    path('abuse/', views.abuse, name='abuse'),
    path('account/', views.account, name='account'),
    path('activities/', views.activities, name='activities'),
    path('adverts/', views.adverts, name='adverts'),
    path('emails/', views.emails, name='emails'),
    path('features/', views.features, name='features'),
    path('info_pages/', views.info_pages, name='info_pages'),
    path('languages/', views.languages, name='languages'),
    path('media/', views.media, name='media'),
    path('messenger/', views.messenger, name='messenger'),
    path('modals/', views.modals, name='modals'),
    path('payments/', views.payments, name='payments'),
    path('payouts/', views.payouts, name='payouts'),
    path('post/', views.post, name='post'),
    path('reels/', views.reels, name='reels'),
    path('timeline/', views.timeline, name='timeline'),
    path('user/', views.user, name='user'),
    #path del admin
    path('admin/', admin.site.urls),
]



