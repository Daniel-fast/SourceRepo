from django.contrib import admin
from .models import Genre, Movie #we´re goint to use these two classes in the same interface of admin
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', "name")

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('id', 'title', 'date_created', 'genre', 'release_year', 'daily_rate',  'number_in_stock')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

