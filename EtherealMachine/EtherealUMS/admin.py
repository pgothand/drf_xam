from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Add the role field to the admin form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Register the CustomUser model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
