from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'last_login',\
		'date_joined', 'is_active')
	
	list_display_links = ('username',)
	ordering = ('date_joined',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)

