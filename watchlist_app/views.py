from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    print(movies.values())
    
    data = {
        'movies': list(movies.values())
    }
    
    return JsonResponse(data)

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    
    data = {
        'movie_name': movie.name,
        'movie_description': movie.description,
        'active': movie.active
    }
    
    return JsonResponse(data)
    
