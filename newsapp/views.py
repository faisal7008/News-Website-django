import email
from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from newsapi.newsapi_client import NewsApiClient
import pandas as pd
from newsdataapi import NewsDataApiClient
import pickle


newsApi = NewsApiClient(api_key='062ed88f7c7848cd8f12d0c060f47190')

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey='pub_7735c82a7317a8d7cb776510a33108bcbcd7')

def home(request):
    response = api.news_api(country='in', category='top', language='en')
    top_news = response['results']
    coronavirusnews = api.news_api(q='covid', category='health', language='en', page=1)
    #print(type(coronavirusnews))
    covidnews = coronavirusnews['results']
    covidnews = covidnews[0:5] 
    #print(type(covidnews))
    # for news in top_news:
    #     print(news)
    #     print()
    return render(request, "home.html", {'top_news':top_news, 'covidnews':covidnews})

def latestnews(request):
    return render(request, "latestnews.html")

def india(request):
    response = api.news_api(country='in', language='en')
    top_news = response['results']
    print('india')
    sources1 = api.sources_api(language='en')
    sources = sources1['results']
    # for source in sources:
    #     print(source['id'])
    # print()
    # for source in sources:
    #     for news in top_news:
    #         if source['id'] == news['source_id']:
    #             print(source['id'], source['name'])
    # for news in top_news:
    #     print(news['source_id'])
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'india', 'sources':sources})

def world(request):
    response = api.news_api(category='world', language='en')
    top_news = response['results']
    print('world')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'world'})

def business(request):
    response = api.news_api(category='business', language='en')
    top_news = response['results']
    print('bussiness')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'bussiness'})

def technology(request):
    response = api.news_api(category='technology', language='en')
    top_news = response['results']
    print('technology')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'technology'})

def entertainment(request):
    response = api.news_api(category='entertainment', language='en')
    top_news = response['results']
    print('entertainment')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'entertainment'})

def sports(request):
    response = api.news_api(category='sports', language='en')
    top_news = response['results']
    print('sports')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'sports'})

def science(request):
    response = api.news_api(category='science', language='en')
    top_news = response['results']
    print('science')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'science'})

def health(request):
    response = api.news_api(category='health', language='en')
    top_news = response['results']
    print('health')
    return render(request, "newstype.html", {'top_news':top_news, 'newstype':'health'})

def newscheck(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        category = request.POST.get('category')
        language = request.POST.get('language')
        country = request.POST.get('country')
        response = api.news_api(q=title, country=country, category=category, language=language)
        top_news = response['results']
        diction = newsfact(title)
        prediction = diction['prediction']
        prob = diction['prob']
        return render(request, "newscheck.html", {'top_news':top_news, 'prediction':prediction,'probability':prob, 'title':str(title)})
    return render(request, "newscheck.html")

def newsfact(var):
    load_model = pickle.load(open('C:\\Users\\faisa\\OneDrive - Chaitanya Bharathi Educational Society\\MP Website\\News Website\\newsapp\\final_model1.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])
    diction = {'prediction':bool(prediction), 'prob':prob}
    # allnews = newsApi.get_everything(q=title(), page_size=100)
    # all_articles = allnews['articles']
    # for i in all_articles:
    #     print(i['title'])
    print("The given statement is ",prediction[0]),
    print("The truth probability score is ",prob[0][1])
    return diction

def about(request):
    return render(request, "about.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            email = request.POST['email']
            password = request.POST['password']
            print(str(email), str(password))
            
            user = authenticate(username=email, password=password)
            
            if user is not None:
                login(request, user)
                #messages.success(request, "Successfully Logged In")
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials")
    return render(request, "signin.html")

def signout(request):
    logout(request)
    #messages.success(request, "You've successfully logged out")
    return redirect("/signin")

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            #username = request.POST['username']
            email = request.POST['email']
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            password1 = request.POST['pass']
            password2 = request.POST['pass1']

            username = email
        
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, "Email Already Registered!!")
            #     return redirect('/register')

            # if User.objects.filter(username=email).exists():
            #     messages.error(request, "Email Already Registered!!")
            #     return redirect('/register')
        
            # if len(username)>20:
            #     messages.error(request, "Username must be under 20 charcters!!")
            #     return redirect('/register')
            
            # if not username.isalnum():
            #     messages.error(request, "Username must be Alpha-Numeric!!")
            #     return redirect('/register')

            # if password1 != password2:
            #     messages.error(request, "Passwords do not match!!")
            #     return redirect('/register')
            try:
                user = User.objects.create_user(username, email, password1)
                user.first_name = first_name.capitalize()
                user.last_name = last_name.capitalize()
                user.save()
                return redirect('/signin')        # render(request, 'sign_in.html') 
            except:
                messages.error(request, "Please Enter neccessary details.")  
                return redirect('/signup')
        return render(request, "signup.html")

def contact(request):
    return render(request, "contact.html")

