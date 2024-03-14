from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # pass
    fieldsets = (
        (
            None, 
            {
                'fields': (
                    'username',
                    'password'
                )
            }
        ),
        (
            'Información Personal',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email'
                    )
            }
        ),
        (
            'otros',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (
            'Redes Sociales', {
                'fields': (
                    'web_site',
                )
            }
        ),
    )
