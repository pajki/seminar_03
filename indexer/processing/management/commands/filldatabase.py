from django.core.management import BaseCommand

from processing.helpers.index_data import Index


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        index = Index()
        index.populate_database()
