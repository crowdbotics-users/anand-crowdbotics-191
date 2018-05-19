
from django.core.management import BaseCommand

from home.models import CustomText, HomePage


def load_initial_data():
    homepage_body = """
        <h1 class="display-4 text-center">anand-crowdbotics-191</h1>
        <p class="lead">
            This is the sample application created and deployed from the crowdbotics slack app. You can
            view list of packages selected for this application below
        </p>"""
    customtext_title = 'anand-crowdbotics-191'
    CustomText.objects.create(title=customtext_title)
    HomePage.objects.create(body=homepage_body)


class Command(BaseCommand):
    can_import_settings = True
    help = 'Load initial data to db'

    def handle(self, *args, **options):
        load_initial_data()
