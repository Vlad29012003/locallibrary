from django.contrib import admin
from catalog.models import Book
from catalog.models import BookInstance
from catalog.models import Author
from catalog.models import Genre

admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth', 'date_of_death')
    fields =  ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author,AuthorAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back' , 'id')
    list_filter = ('status','due_back')

    fieldsets = (
        (None,{
            'fields': ('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back')
        }),
    )   

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inline = [BookInstanceInline]



class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')


    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
    