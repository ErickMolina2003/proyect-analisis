"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name',
                    'is_staff', 'phone_number', 'is_active', ]
    fieldsets = (
        (None, {'fields': ('email', 'dni', 'first_name', 'last_name',
         'phone_number', 'rtn', 'position', 'address',  'password',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'hire_date', )}),
    )
    readonly_fields = ['last_login', ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'dni',
                'first_name',
                'last_name',
                'rtn',
                'birth_date',
                'hire_date',
                'position',
                'phone_number',
                'address',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Partner)
admin.site.register(models.Motorist)
admin.site.register(models.Truck)
admin.site.register(models.Client)
admin.site.register(models.Freight)
admin.site.register(models.Billing)
admin.site.register(models.Commission)
