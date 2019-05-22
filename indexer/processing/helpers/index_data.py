from indexer.processing.helpers.processing import Processing
import os
from os.path import realpath, dirname
from os import listdir
from os.path import isfile, join


def get_list_of_input_files():
    path = dirname(dirname(dirname(realpath(__file__)))) + "/data"
    dir_list = [f for f in listdir(path)]
    files = []

    for d in dir_list:
        current_path = path + "/" + d
        files.extend([current_path + "/" + f for f in listdir(current_path) if isfile(join(current_path, f))])

    # use only html files
    files = [f for f in files if f.split(".")[-1] == "html"]

    # print(files)
    return files


class Index:
    def __init__(self, list_data):
        # self.data = enumerate(list_data)
        self.data = None

    def get_indexes(self, word):
        # TODO fix
        indexes = [i for i, x in self.data if x == word]
        return indexes, len(indexes)

    def populate_database(self):
        # init module
        p = Processing()

        # find all files
        all_files = get_list_of_input_files()

        # extract text and process it
        for f in all_files:
            print("Opening file: " + f)
            content = p.get_text_from_web_page(f)
            print("Processing text")
            token_list = p.process_text(content)
            print(token_list)
            # save enumerated token list to self
            self.data = enumerate(token_list)

            for word in token_list:
                indexes, indexes_len = self.get_indexes(word)
                print(f, indexes, indexes_len)
            break



        # get indexes
        # save to DB

        pass




if __name__ == "__main__":
    i = Index(None)
    i.populate_database()

