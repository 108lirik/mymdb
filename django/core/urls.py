from django.urls import paths

from . import views

app_name = 'core'
url_patterns = [
    path('movies',
    views.MovieList.as_view(),
    name='MovieList'),
]
