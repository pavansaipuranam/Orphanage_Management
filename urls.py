from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('show/<int:show_id>/', views.show_detail, name='show_detail'),
    path('watch/movie/<int:movie_id>/', views.watch_movie, name='watch_movie'),
    path('watch/show/<int:show_id>/episode/<int:episode_id>/', views.watch_episode, name='watch_episode'),
    path('watchlist/add/<str:content_type>/<int:content_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<str:content_type>/<int:content_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('review/<str:content_type>/<int:content_id>/', views.add_review, name='add_review'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('browse/', views.browse, name='browse'),
] 