from django.contrib import admin
from .models import Category, Genre, Movie, Reviews, RatingStar, Rating, Actor, MovieShots


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Actor)
admin.site.register(MovieShots)
