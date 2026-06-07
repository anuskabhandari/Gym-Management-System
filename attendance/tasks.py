
from datetime import datetime

from celery import shared_task

from attendance.models import Attendance
from member.models import Member


@shared_task
def add_attendance():
    member = Member.objects.filters(is_active=True)
    for i in member:
        attendance = Attendance.objects.create(
            member =i,
            attendance_date = datetime.now().date(),

        )
    return True   


@shared_task
def mark_member_attendance():
    attendance = Attendance.objects.all()
    for i in attendance:
        if i.check_in:
            i.is_present = True
            if not i.check_out:
                i.check_out = datetime.now().time()

            i.save(update_fields=['is_present','check_out'])    
        