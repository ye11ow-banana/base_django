from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "user"
    list_display_links = "user",


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = "title", "author", "draft", "get_image"
    list_filter = "author",
    search_fields = "title", "genre__title"
    readonly_fields = "author",
    save_on_top = True
    save_as = True
    list_editable = "draft",
    actions = "make_published", "make_unpublished"

    fieldsets = (
        (None, {
            "fields": (("title", "draft"), )
        }),
        ("Images", {
            "fields": ("poster", ),
        }),
        ("Relations", {
            "classes": ("collapse", ),
            "fields": ("author", "genre")
        }),
    )

    @staticmethod
    def get_image(obj):
        return mark_safe(
            f'<img src={obj.poster.url} width="50" height="60"'
        )

    @staticmethod
    def send_created_message(self, request, row_update):
        ms = '1 note was' if row_update == 1 else f'{row_update} notes were'
        self.message_user(request, ms + ' updated')

    def make_published(self, request, queryset):
        row_update = queryset.update(draft=False)
        self.send_created_message(self, request, row_update)

    def make_unpublished(self, request, queryset):
        row_update = queryset.update(draft=True)
        self.send_created_message(self, request, row_update)

    make_published.short_description = "Make published"
    make_published.allowed_permissions = "change",

    make_unpublished.short_description = "Make unpublished"
    make_unpublished.allowed_permissions = "change",


admin.site.register(Genre)

admin.site.site_title = "Base django"
admin.site.site_header = "Base django"
