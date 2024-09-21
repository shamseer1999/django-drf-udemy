from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import (WatchListListView,WatchListListDetailView,SreamPlatformView,SreamPlatformDetailView,
                                     ReviewsList,ReviewDetail,ReviewCreate)


urlpatterns = [
    path('list/' , WatchListListView.as_view(), name='watch_list'),
    path('<int:watchlist_id>', WatchListListDetailView.as_view(), name='watchlist_id'),
    path('stream/' , SreamPlatformView.as_view(), name='platform_list'),
    path('stream/<int:pk>', SreamPlatformDetailView.as_view(), name='platform_id'),
    # path('reviews/', ReviewsList.as_view(), name='reviews'),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='create_review'),
    path('<int:pk>/review/', ReviewsList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review')
]