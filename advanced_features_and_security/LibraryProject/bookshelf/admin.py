from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'publication_year')
    list_filter = ("publication_year",)
    search_fields = ("author",)

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(DefaultUserAdmin):
    model = CustomUser
    fieldsets = (
        DefaultUserAdmin.fieldsets + (
            # (None, {'fields': ('date_of_birth', 'profile_photo')}),
            (None, {'fields': ('email', 'password', 'username')}),
    ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        )

    )
    add_fieldsets = (
        # DefaultUserAdmin.add_fieldsets + (None, {'fields':('date_of_birth')})
         (None, {
      'classes': ('wide',),
      'fields': ('email', 'username', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
    }),
    )
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
























admin.site.register(CustomUser, CustomUserAdmin)