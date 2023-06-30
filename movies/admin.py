from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, Reviews, RatingStar, Rating, Actor, MovieShots


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'emails')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="auto"')

    get_image.short_description = 'Image'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    readonly_fields = ('get_image', )
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline', 'category'),)
        }),
        (None, {
            'fields': ('description', ('get_image', 'poster'))
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="auto"')

    get_image.short_description = 'Image'


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'emails', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'emails')


@admin.register(Genre)
class ReviewGenre(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Actor)
class ReviewActor(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="auto"')

    get_image.short_description = 'Image'


@admin.register(Rating)
class ReviewRating(admin.ModelAdmin):
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class ReviewMovieShots(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="auto"')

    get_image.short_description = 'Image'


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(Reviews)
# admin.site.register(Rating)
# admin.site.register(Actor)
# admin.site.register(MovieShots)
admin.site.register(RatingStar)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
