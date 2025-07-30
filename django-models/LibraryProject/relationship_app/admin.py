from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

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