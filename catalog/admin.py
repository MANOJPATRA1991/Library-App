from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.StackedInline):
    """
    Inline editing of Book model
    """
    model = Book
    extra = 0


#  Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [
        BookInline
    ]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    """
    Inline editing of BookInstance model
    """
    model = BookInstance
    readonly_fields = ['id']
    extra = 0


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [
        BookInstanceInline
    ]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
    readonly_fields = ['id']
