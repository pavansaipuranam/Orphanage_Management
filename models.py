from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    poster = models.ImageField(upload_to='movie_posters/')
    backdrop = models.ImageField(upload_to='movie_backdrops/')
    video_url = models.URLField()
    genres = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TVShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='show_posters/')
    backdrop = models.ImageField(upload_to='show_backdrops/')
    genres = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Episode(models.Model):
    show = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    episode_number = models.IntegerField()
    season_number = models.IntegerField()
    description = models.TextField()
    video_url = models.URLField()
    duration = models.IntegerField(help_text="Duration in minutes")
    thumbnail = models.ImageField(upload_to='episode_thumbnails/')
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.show.title} - S{self.season_number}E{self.episode_number}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)
    watchlist = models.ManyToManyField(Movie, related_name='watchlisted_by')
    watchlist_shows = models.ManyToManyField(TVShow, related_name='watchlisted_by')
    continue_watching = models.ManyToManyField(Movie, related_name='watching_by')
    continue_watching_shows = models.ManyToManyField(TVShow, related_name='watching_by')
    last_watched_episode = models.ForeignKey(Episode, on_delete=models.SET_NULL, null=True, blank=True)
    subscription_status = models.CharField(max_length=20, choices=[
        ('free', 'Free'),
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('ultra', 'Ultra')
    ], default='free')
    subscription_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    show = models.ForeignKey(TVShow, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.movie.title if self.movie else self.show.title}"

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    watched_at = models.DateTimeField(auto_now_add=True)
    watch_duration = models.IntegerField(help_text="Duration watched in seconds")

    def __str__(self):
        return f"{self.user.username} watched {self.movie.title if self.movie else self.episode.title}" 