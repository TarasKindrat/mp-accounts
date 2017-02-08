
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from accounts.admin import views


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.register_view(
    'accounts/user-statistic', views.user_statistic, 'user-statistic')
