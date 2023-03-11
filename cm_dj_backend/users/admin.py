from django.contrib import admin
from users import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
      list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
      list_filter = ('is_staff', 'is_active')
      search_fields = ('username', 'email', 'first_name', 'last_name')
      ordering = ('-date_joined',)
      filter_horizontal = ()
      fieldsets = ()


