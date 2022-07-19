from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all() # this returns a query - and will be used in the future - it´s called 'Lazy Loading' - so, this queryset is a 'Lazy Object'
        resource_name = 'movies'
        excludes = ['date_created']




# Create your models here.
