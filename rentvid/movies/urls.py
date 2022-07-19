from django.urls import path
from . import views

# movies/
# movies/1/details

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'), #this is the root of the url
    path('<int:movie_id>', views.detail, name='detail')

]