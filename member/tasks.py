from celery import shared_task

from member.models import Member

@shared_task
def mark_all_member_active():
    member = Member.objects.all()
    member.update(is_active= True)
    return member