from django.core.mail import send_mail
from django.core.management import BaseCommand


def main():
    send_mail(
        'hi', 'I like you', 'your friend', ['frqhero@gmail.com']
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
