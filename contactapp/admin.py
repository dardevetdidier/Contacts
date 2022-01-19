from django.contrib import admin
from .models import Contact, Group


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "phone",
        "email",
        "group",
        "date_created"
    ]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]