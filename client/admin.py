from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'password', 'email', 'birth_date'
    )
    # search_fields = ['user', 'session', 'action']
    # list_filter = ['user', 'session', 'action']


admin.site.register(User, ClientAdmin)
