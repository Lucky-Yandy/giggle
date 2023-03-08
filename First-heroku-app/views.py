from datetime import datetime

import requests
from django.shortcuts import render


def homepage(request):
    context = {
    }
    return render(request, 'homepage.html', context)


def search_results(request):

    search_type = request.GET['stype']
    search_query = request.GET['searchterm']

    context = {
        'result_count': 0,
        'search_message': None,
        'search_term': search_query,
        'search_type': search_type,
    }

    if search_type == 'booksearch':
        context['search_message'] = 'Books'
        context['results_count'] = 0
        url ='http://openlibrary.org/search.json?q='
        url+=search_query
        response = requests.get(url)
        books_data = response.json() 
        results_list = books_data['docs']
        context['results_count']= books_data['numFound']
        print( results_list)
        context ['books_results']= results_list
        
        
        

    elif search_type == 'newssearch':
        context['search_message'] = 'Headlines'
      
        url = 'http://content.guardianapis.com/search?api-key=a938fccc-00e9-41ca-905c-741615da8be1&page-size=50&q='
        url+=search_query
        response = requests.get(url)
        news_data = response.json() 
        results_list = news_data['response']['results']
        context['results_count']=news_data['response']['total']
        print( results_list)
        context ['news_results']= results_list
    
        

    elif search_type == 'musicsearch':
        context['search_message'] = 'Music'
        #context['results_count'] = 0
        # API example: http://musicbrainz.org/ws/2/release/?fmt=json&query=cardi+b
        # TODO Unfinished...
        url='http://musicbrainz.org/ws/2/release/?fmt=json&query='
        url+=search_query
        response = requests.get(url)
        music_data = response.json() 
        results_list = music_data['releases']
        context['results_count']= music_data['count']
        print( results_list)
        context ['music_results']= results_list
        
    else:
        context['search_message'] = 'Unknown search, bug?'

    return render(request, 'search_results.html', context)


def giggle_news(request):

    
    url = 'http://content.guardianapis.com/search?api-key=a938fccc-00e9-41ca-905c-741615da8be1&page-size=50'
    response = requests.get(url)
    news_data = response.json() 
    results_list = news_data['response']['results']
    context = {
        'news_results': results_list,
    }
    return render(request, 'news.html', context)

