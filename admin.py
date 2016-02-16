from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Movies,Director,Category



# Register your models here.

class MoviesAdmin(admin.ModelAdmin,AdminVideoMixin):
        prepopulated_fields = {'slug': ('Title',)}
        list_display = ('Title','Releasedate', 'publisheddate', 'director')
        list_display_links = ('Title','Releasedate', 'publisheddate', 'director')
        search_fields = ['Title']


class DirectorAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('Name',)}
        list_display =('Name','Deteborn')
        search_fields = ['Name']


class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('categorytitle',)}
        search_fields = ['categorytitle']



admin.site.register(Movies,MoviesAdmin)
admin.site.register(Director,DirectorAdmin)
admin.site.register(Category,CategoryAdmin)
