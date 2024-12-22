from django.contrib import admin
# from django.contrib.auth.models import Permission,Group
# Register your models here.
from .models import CustomUser,Permission,Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
    
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_editor",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "is_editor", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


# Personnaliser l'affichage dans l'admin pour lier les permissions
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')
    search_fields = ('name', 'codename')

# Personnaliser l'admin de Groupes pour y afficher les permissions personnalisées
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)  # Pour afficher les permissions de manière plus simple

# admin.site.unregister(Group)
# admin.site.register(Group, GroupAdmin)