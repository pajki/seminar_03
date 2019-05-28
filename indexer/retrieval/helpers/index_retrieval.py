from datetime import datetime

from processing.helpers.processing import Processing
from processing.models import Posting


class IndexRetrieval:

    def __init__(self, query):
        self.query = query

        self.processing = Processing()

        self.query_words = None
        self.results = []

    def run(self):
        """
        Run the class.
        """
        s = datetime.now()
        self.process_query()
        self.get_results()
        self.get_snippets()
        running_time = datetime.now() - s
        self.print_results(running_time)

    def process_query(self):
        """
        Process the given query.
        """
        self.query_words = self.query.lower().split(" ")

    def get_results(self):
        """
        Query each word from given query and find 5 most relevant documents.
        """
        hits = {}
        indices = {}
        for word in self.query_words:
            documents = list(Posting.objects.filter(word__word=word))
            for document in documents:
                if document.document_name in hits.keys():
                    hits[document.document_name] += document.frequency
                    indices[document.document_name] += document.indexes
                else:
                    hits[document.document_name] = document.frequency
                    indices[document.document_name] = document.indexes

        results = [
            {"document": "not a doc 1", "count": -1},
            {"document": "not a doc 2", "count": -1},
            {"document": "not a doc 3", "count": -1},
            {"document": "not a doc 4", "count": -1},
            {"document": "not a doc 5", "count": -1},
        ]

        for key, value in zip(hits.keys(), hits.values()):
            for i in range(0, len(results)):
                if results[i]["count"] < value:
                    results[i] = {"document": key, "count": value, "indices": indices[key]}
                    break

        for result in results:
            if result["count"] > 0:
                self.results.append(result)

    def get_snippets(self):
        """
        Use processing class to get 3 word snippets, before and after the query word.
        """
        for result in self.results:
            text = self.processing.get_text_from_web_page(result["document"]).split(" ")
            snippets = []
            for index in [int(x) for x in result["indices"].split(",")]:
                snippets.append(" ".join(text[index-2:index+4]))
            result["snippets"] = snippets

    def print_results(self, running_time):
        """
        Print 5 most relevant results.
        """
        longest_document = max([len("/".join(x["document"].split("/")[-2:])) for x in self.results])

        print('Results for a query: "{}"'.format(self.query))
        print()
        print()
        print("\tResults found in {}ms.".format(round(running_time.microseconds / 1000)))
        print()
        print()
        print("\tFrequencies Document {} Snippet".format(" " * (longest_document - 9)))
        print("\t----------- {} {}".format("-" * longest_document, "-" * 200))
        for result in self.results:
            print("\t{}{} {}".format(str(result["count"]).ljust(12, " "),
                                    "/".join(result["document"].split("/")[-2:]).ljust(longest_document, " "),
                                     (" ... ".join(result["snippets"])[0:200])))
