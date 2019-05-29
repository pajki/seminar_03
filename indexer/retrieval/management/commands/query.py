from django.core.management import BaseCommand

from retrieval.helpers.index_retrieval import IndexRetrieval


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_query', type=str, help='The query for which the program will return results.')

    def handle(self, *args, **kwargs):
        retrieval = IndexRetrieval(kwargs["user_query"])
        retrieval.run()
