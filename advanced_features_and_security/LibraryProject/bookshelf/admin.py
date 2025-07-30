from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'publication_year')
    list_filter = ("publication_year",)
    search_fields = ("author",)

admin.site.register(Book, BookAdmin)

class UserAdmin(DefaultUserAdmin):
    model = User
    fieldsets = (
        DefaultUserAdmin.fieldsets + (
            (None, {'fields': ('date_of_birth', 'profile_photo')})
        )

    )
    add_fieldsets = (
        DefaultUserAdmin.add_fieldsets + (None, {'fields':('date_of_birth')})
    )


admin.site.register(User, UserAdmin)