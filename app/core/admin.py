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


class PartnerAdmin(admin.ModelAdmin):
    """Define admin pages for partners"""
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name',
                    'phone_number', 'is_active', ]


class MotoristAdmin(admin.ModelAdmin):
    """Define admin pages for partners"""
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name',
                    'phone_number', 'is_active', ]


class TruckAdmin(admin.ModelAdmin):
    """Define admin pages for Trucks"""
    ordering = ['id']
    list_display = ['truck_number', 'is_active', ]


class ClientAdmin(admin.ModelAdmin):
    """Define admin for clients"""
    ordering = ['id']
    list_display = ['first_name', 'last_name',
                    'address', 'rtn', 'phone_number', 'email']


class FreightAdmin(admin.ModelAdmin):
    """Define admin for Freight"""
    list_display = ['id_client', 'id_partner',
                    'id_motorist', 'id_truck', 'sub_total', 'isv',
                    'total', 'is_completed']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Partner, PartnerAdmin)
admin.site.register(models.Motorist, MotoristAdmin)
admin.site.register(models.Truck, TruckAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Freight, FreightAdmin)
admin.site.register(models.Billing)
admin.site.register(models.Commission)
