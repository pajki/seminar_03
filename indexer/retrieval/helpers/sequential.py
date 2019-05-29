import sys,os
from indexer.processing.helpers.processing import Processing
from datetime import datetime
import re


class Sequential:
    def __init__(self):
        self.processing = Processing()
        self.full_query = ""
        self.query = []
        self.files = []
        self.results = []

    def run(self):

        start = datetime.now()
        self.process_files()
        self.find_top_frequencies()
        self.find_snippets()
        running_time = datetime.now() - start
        self.print_results(running_time)

    def set_query(self, q):
        self.full_query = q
        self.query = q.lower().split(' ')

    def set_dir(self, folder_name):
        for path, subdirs, files in os.walk(folder_name):
            for name in files:
                self.files.append(os.path.join(path, name))

    def process_files(self):
        self.files = [(file, self.processing.get_text_from_web_page(file)) for file in self.files[0:50]]

    def find_top_frequencies(self):

        freqs = []
        for file in self.files:
            f = 0
            for word in self.query:
                f += self.processing.process_text(file[1]).count(word)
            freqs.append((file[0], file[1], f))

        freqs.sort(key=lambda tup: tup[2], reverse=True)

        self.results = freqs[0:5]

    def find_snippets(self):

        r = []
        for result in self.results:
            text = self.processing.get_text_from_web_page(result[0]).split(" ")
            snippets = []
            prev_index = -42
            for index in [i for i, x in enumerate(text) if re.sub('[^A-Za-z0-9]+', '', x).lower() in self.query]:
                if index != prev_index+1:
                    snippets.append(" ".join(text[index - 2:index + 4]))
                prev_index = index
            r.append((result[0], result[1], result[2], snippets))

        self.results = r

    def print_results(self, running_time):
        """
        Print 5 most relevant results.
        """
        longest_document = max([len("/".join(x[0].split("/")[-2:])) for x in self.results])

        print('Results for a query: "{}"'.format(self.full_query))
        print()
        print()
        print("\tResults found in {}s {}ms.".format(running_time.seconds,
                                                          round(running_time.microseconds / 1000)))
        print()
        print()
        print("\tFrequencies Document {} Snippet".format(" " * (longest_document - 9)))
        print("\t----------- {} {}".format("-" * longest_document, "-" * 200))
        for result in self.results:
            print("\t{}{} {}".format(str(result[2]).ljust(12, " "),
                                     "/".join(result[0].split("/")[-2:]).ljust(longest_document, " "),
                                     (" ... ".join(result[3])[0:200])))


if __name__ == "__main__":
    print("running sequential retrieve module\n")

    s = Sequential()
    s.set_query("Sistem SPOT")
    s.set_dir("../../data")
    s.run()



