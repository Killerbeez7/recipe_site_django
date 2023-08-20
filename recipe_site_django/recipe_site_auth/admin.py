# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from recipe_site_django.profiles.models import UserModel
#
#
# @admin.register(UserModel)
# class RecipeSiteAdmin(UserAdmin):
#     list_display = ('email', 'is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'groups')
#     ordering = ('email',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {
#             'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
#
#         }),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
