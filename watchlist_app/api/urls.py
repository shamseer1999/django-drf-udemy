from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import WatchListListView,WatchListListDetailView,SreamPlatformView,SreamPlatformDetailView


urlpatterns = [
    path('list/' , WatchListListView.as_view(), name='watch_list'),
    path('<int:movie_id>', WatchListListDetailView.as_view(), name='watchlist_id'),
    path('platforms/' , SreamPlatformView.as_view(), name='platform_list'),
    path('platforms/<int:platform_id>', SreamPlatformDetailView.as_view(), name='platform_id'),
]