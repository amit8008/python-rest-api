from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import ShowListAV, ShowDetailAV, StreamPlatformListAV

urlpatterns = [
    path('list/', ShowListAV.as_view(), name='show-list'),
    path('<int:pk>', ShowDetailAV.as_view(), name='show-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='Stream'),
]
