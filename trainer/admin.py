from django.contrib import admin

from trainer.models import Trainer

# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'experience_years',
        'salary',
        'joining_date',
        'is_active',
    )

    search_fields = (
        'full_name',
        'email',
        'phone',
        'specialization',
    )

    list_filter = (
        'is_active',
        'joining_date',
    )

    ordering = ('full_name',)

    list_editable = (
        'is_active',
        'salary',
    )