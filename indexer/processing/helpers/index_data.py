from processing.helpers.processing import Processing
import os
from os.path import realpath, dirname
from os import listdir
from os.path import isfile, join

from processing.models import IndexWord, Posting


def get_list_of_input_files():
    """
    Helper function
    Returns all input files in a array as file path (only HTML files)
    :return: array of file paths
    """
    path = dirname(dirname(dirname(realpath(__file__)))) + "/data"
    dir_list = [f for f in listdir(path)]
    files = []

    for d in dir_list:
        current_path = path + "/" + d
        files.extend([current_path + "/" + f for f in listdir(current_path) if isfile(join(current_path, f))])

    # use only html files
    files = [f for f in files if f.split(".")[-1] == "html"]
    return files


class Index:
    def __init__(self):
        pass

    def get_indices(self, data_list):
        """
        Returns where token is located in a document
        :param data_list: tokenized input
        :return: {'skupnopiškotki': [52], 'vlade': [21], 'spletnega': [86, 132], 'pregrada': [114], ...}
        """
        unique_entries = set(data_list)
        indices = {value.lower(): [i for i, v in enumerate(data_list) if v == value] for value in unique_entries}
        return indices

    def populate_database(self):
        """
        This function populates database with data
        """
        # init module
        p = Processing()

        # find all files
        all_files = get_list_of_input_files()

        # extract text and process it
        i = 1
        n = len(all_files)

        for f in all_files:
            print("Processing file {}/{}: {}".format(i, n, "/".join(f.split("/")[-2:])))
            # get content
            content = p.get_text_from_web_page(f)
            # get tokens
            token_list = p.process_text(content)
            # get indices from content - to be able to later create snippets
            indices = self.get_indices(content.split(" "))
            for key, value in zip(indices.keys(), indices.values()):
                # only insert tokens into the db
                if key in token_list:
                    word, created = IndexWord.objects.get_or_create(word=key)
                    value = [str(x) for x in value]
                    Posting(word=word, document_name=f, frequency=len(value), indexes=",".join(value)).save()
            i += 1


if __name__ == "__main__":
    index = Index()
    index.populate_database()

