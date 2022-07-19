from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    #These methods representes the Database abstraction API that django has
    movies = Movie.objects.all() #django renders this command: SELECT * FROM movies_movie and we are using a list 'movies' to hold that

    return render(request, 'movies/index.html', {'movies': movies }) # instead of using the 'return HttpResponse(output)' we´re going to use templates to render HTML


    # output = ', '.join([m.title for m in movies]) #Now we´re going to use a list comprehension to get the title of these movies
    #       we are using a comma to separate the list and the function 'join()' - ', '.join



    # Movie.objects.filter(release_year=1984)#django renders this command: SELECT * FROM movies_movie WHERE release_year=1984
    # Movie.object.get(id=1)
    # return HttpResponse(output)
    # return HttpResponse("Hello World, get ready for me!")

def detail(request, movie_id):
    return HttpResponse(movie_id)
