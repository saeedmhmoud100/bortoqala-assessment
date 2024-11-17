from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "personal info",
            {
                'fields': (
                    'phone_number',
                    'address',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
