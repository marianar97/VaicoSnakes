# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):


    list_display = ('user', 'business', 'phone_number', 'picture')
    search_fields = (
        'user__email',
        'user__username', 
        'user__first_name', 
        'user__last_name',
        'phone_number'
     )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (('business','phone_number'),)
        }),
        ('Meta data', {
            'fields': (('created','modified'),)
        })

    )

    readonly_fields = ('created','modified',)

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

