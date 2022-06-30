from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   #path('', views.index, name='index'),
    #path('', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('headlines', views.india, name='headlines'),
    path('sports', views.sports, name='sports'),
    path('india', views.india, name='india'),
    path('world', views.world, name='world'),
    path('business', views.business, name='business'),
    path('technology', views.technology, name='technology'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('science', views.science, name='science'),
    path('health', views.health, name='health'),
    path('newscheck', views.newscheck, name='newscheck'),
    path('about', views.about, name='about'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       # For storing files