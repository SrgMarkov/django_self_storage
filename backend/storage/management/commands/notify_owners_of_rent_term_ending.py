from datetime import timedelta

from django.template.loader import render_to_string
from django.utils import timezone

from django.core.mail import EmailMultiAlternatives
from django.core.management import BaseCommand
from django.utils.html import strip_tags

from storage.models import BoxX


def prepare_send_email(email, context):
    subject = 'Rent Term Ending Soon'

    html_content = render_to_string('email_template.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject,
        text_content,
        'Self Storage',
        [email],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()


def main():
    current_time = timezone.now().date()
    month_later = current_time + timedelta(days=30)
    boxes_expire_in_month = BoxX.objects.filter(end_date__date=month_later)
    for box_expire_in_month in boxes_expire_in_month:
        user_profile = box_expire_in_month.user_box.first()
        email = user_profile.user.email
        context = {
            'end_date': month_later,
            'name': user_profile.user.first_name
            if user_profile.user.first_name
            else 'dear client',
        }
        prepare_send_email(email, context)


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
