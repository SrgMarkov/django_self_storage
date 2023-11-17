from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand


def main():
    send_mail(
        'hi', 'I like you', settings.EMAIL_HOST_USER, ['frqhero@gmail.com']
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
