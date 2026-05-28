from django.contrib import admin

from member.models import Member

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "gender",
        "blood_group",
        "is_active",
        "joined_at",
    )

    list_filter = (
        "gender",
        "blood_group",
        "is_active",
        "joined_at",
    )

    search_fields = (
        "first_name",
        "middle_name",
        "last_name",
        "phone",
        "email",
    )

    ordering = ("-joined_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Personal Information", {
            "fields": (
                "first_name",
                "middle_name",
                "last_name",
                "dob",
                "gender",
            )
        }),

        ("Contact Information", {
            "fields": (
                "phone",
                "email",
                "emergency_contact",
                "address",
            )
        }),

        ("Health Information", {
            "fields": (
                "height_cm",
                "weight_kg",
                "blood_group",
                "medical_conditions",
            )
        }),

        ("Membership Details", {
            "fields": (
                "is_active",
                "joined_at",
            )
        }),

        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )