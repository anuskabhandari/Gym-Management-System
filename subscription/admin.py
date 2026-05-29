from django.contrib import admin

# Register your models here.
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'days',
        'price',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'created_at',
    )

    search_fields = (
        'name',
    )

    ordering = (
        '-created_at',
    )

    list_editable = (
        'price',
        'is_active',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )