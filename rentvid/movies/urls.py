from django.urls import path
from . import views

# movies/
# movies/1/details


urlpatterns = [
    path('', views.index, name='movies_index'), #this is the root of the url
    path('<movie_id>', views.detail, name='movies_detail')

]