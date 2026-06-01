from django.contrib import admin

from attendance.models import Attendance

# Register your models here.


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'member',
        'attendance_date',
        'check_in',
        'check_out',
        'is_present',
        'created_at',
    )
    list_filter = (
        'is_present',
        'attendance_date',
        'created_at',
    )
    search_fields = (
        'member__first_name',
        'member__last_name',
    )
    ordering = ('-attendance_date',)
    date_hierarchy = 'attendance_date'