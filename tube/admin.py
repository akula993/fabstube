from django.contrib import admin
from django.utils.safestring import mark_safe

from tube.models import Category, Language, Tag, Video, Playlist, Channel


class VideoInline(admin.StackedInline):
    """Интро на странице фильтра"""
    model = Video
    extra = 0
    prepopulated_fields = {'slug': ('file',), }

    # fields = (('title', "slug"), "about", 'file', ('language_in_video', 'category', 'tags', 'playlist',),)
    show_change_link = True
    # readonly_fields = ('get_image',)
    verbose_name = 'Добавить интро?'
    verbose_name_plural = 'Добавить интро?'
    # template = 'base.html'
    # min_num = 0
    # max_num = 2
    #
    # def get_image(self, obj, ):
    #     return mark_safe(f'<img src={obj.image.url} width="100px height=auto">')
    #
    # get_image.short_description = "Изображение"
    fieldsets = (
        ('Заголовок и URL', {
            'fields': (('file', 'slug'),),
            'description': "Обязательно для заполнение, URL подставляется автоматически."
        }),
        ('Описание', {
            'fields': ('about',),

            'classes': ('collapse', 'wide'),
            'description': "При желании заполните текст."
        }),
        ('Об аппарате', {
            'classes': ('collapse',),
            'fields': (('language_in_video', 'category','tags', 'playlist',),),
            # 'description': "Укажите доп сведения об аппарате."
        }),
    )


class PlaylistInline(admin.TabularInline):
    """Интро на странице фильтра"""
    model = Playlist


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'slug', 'language_in_video',)
    list_display_links = ('id', 'file')

    prepopulated_fields = {'slug': ('file',), }
    save_on_top = True
    actions_on_top = True
    save_as = True


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    list_filter = ('video__file',)
    # search_fields = ('video__title',)
    # list_editable = ('power', 'number_of_mode',)
    # prepopulated_fields = {'url': ('name',), }
    save_on_top = True
    actions_on_top = True
    save_as = True
    inlines = [VideoInline]


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image',)
    list_display_links = ('id', 'user',)
