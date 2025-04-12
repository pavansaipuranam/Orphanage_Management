from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Movie, TVShow, Genre, UserProfile, Review, WatchHistory
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    trending_movies = Movie.objects.order_by('-views')[:8]
    popular_shows = TVShow.objects.order_by('-views')[:8]
    genres = Genre.objects.all()
    
    context = {
        'trending_movies': trending_movies,
        'popular_shows': popular_shows,
        'genres': genres,
    }
    return render(request, 'html/netflix.html', context)

@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    related_movies = Movie.objects.filter(genres__in=movie.genres.all()).exclude(id=movie_id)[:4]
    reviews = Review.objects.filter(movie=movie)
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(movie=movie, user=request.user).first()
    
    context = {
        'movie': movie,
        'related_movies': related_movies,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'html/movie_detail.html', context)

@login_required
def show_detail(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    episodes = show.episodes.all().order_by('season_number', 'episode_number')
    reviews = Review.objects.filter(show=show)
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(show=show, user=request.user).first()
    
    context = {
        'show': show,
        'episodes': episodes,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'html/show_detail.html', context)

@login_required
def watch_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.views += 1
    movie.save()
    
    # Record watch history
    WatchHistory.objects.create(
        user=request.user,
        movie=movie,
        watch_duration=0
    )
    
    context = {
        'movie': movie,
    }
    return render(request, 'html/player.html', context)

@login_required
def watch_episode(request, show_id, episode_id):
    show = get_object_or_404(TVShow, id=show_id)
    episode = get_object_or_404(Episode, id=episode_id, show=show)
    episode.views += 1
    episode.save()
    
    # Record watch history
    WatchHistory.objects.create(
        user=request.user,
        episode=episode,
        watch_duration=0
    )
    
    context = {
        'show': show,
        'episode': episode,
    }
    return render(request, 'html/player.html', context)

@login_required
def add_to_watchlist(request, content_type, content_id):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if content_type == 'movie':
        content = get_object_or_404(Movie, id=content_id)
        user_profile.watchlist.add(content)
    else:
        content = get_object_or_404(TVShow, id=content_id)
        user_profile.watchlist_shows.add(content)
    
    return JsonResponse({'status': 'success'})

@login_required
def remove_from_watchlist(request, content_type, content_id):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if content_type == 'movie':
        content = get_object_or_404(Movie, id=content_id)
        user_profile.watchlist.remove(content)
    else:
        content = get_object_or_404(TVShow, id=content_id)
        user_profile.watchlist_shows.remove(content)
    
    return JsonResponse({'status': 'success'})

@login_required
def add_review(request, content_type, content_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if content_type == 'movie':
            content = get_object_or_404(Movie, id=content_id)
            Review.objects.create(
                user=request.user,
                movie=content,
                rating=rating,
                comment=comment
            )
        else:
            content = get_object_or_404(TVShow, id=content_id)
            Review.objects.create(
                user=request.user,
                show=content,
                rating=rating,
                comment=comment
            )
        
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'})

def search(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    shows = TVShow.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    
    context = {
        'query': query,
        'movies': movies,
        'shows': shows,
    }
    return render(request, 'html/search.html', context)

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    watch_history = WatchHistory.objects.filter(user=request.user).order_by('-watched_at')[:10]
    
    context = {
        'user_profile': user_profile,
        'watch_history': watch_history,
    }
    return render(request, 'html/profile.html', context)

def browse(request):
    genre_id = request.GET.get('genre')
    content_type = request.GET.get('type', 'all')
    
    movies = Movie.objects.all()
    shows = TVShow.objects.all()
    
    if genre_id:
        genre = get_object_or_404(Genre, id=genre_id)
        movies = movies.filter(genres=genre)
        shows = shows.filter(genres=genre)
    
    if content_type == 'movies':
        shows = None
    elif content_type == 'shows':
        movies = None
    
    context = {
        'movies': movies,
        'shows': shows,
        'genres': Genre.objects.all(),
        'selected_genre': genre_id,
        'content_type': content_type,
    }
    return render(request, 'html/browse.html', context) 