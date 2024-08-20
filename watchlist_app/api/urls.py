from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import MovieListView,MovieDetailView


urlpatterns = [
    path('list/' , MovieListView.as_view(), name='movie_list'),
    path('<int:movie_id>', MovieDetailView.as_view(), name='movie_id'),
]