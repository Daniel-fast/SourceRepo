from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
    movie = get_object_or_404(Movie, pk=movie_id)
        # return HttpResponse(movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
   
    # try: Instead of using a try block, django has a function to do this, let´s import a new module
    #     movie = Movie.objects.get(pk=movie_id)
    #     # return HttpResponse(movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()    


