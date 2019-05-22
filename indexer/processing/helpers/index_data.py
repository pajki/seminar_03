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
    def __init__(self):
        pass

    def get_indices(self, data_list):
        unique_entries = set(data_list)
        indices = {value: [i for i, v in enumerate(data_list) if v == value] for value in unique_entries}
        # print(indices)
        return indices

    def populate_database(self):
        # init module
        p = Processing()

        # find all files
        all_files = get_list_of_input_files()

        # extract text and process it
        for f in all_files:
            # get content
            print("Opening file: " + f)
            content = p.get_text_from_web_page(f)

            # get tokens
            print("Processing text")
            token_list = p.process_text(content)
            # print(token_list)

            # get indices
            indices = self.get_indices(token_list)
            print(indices)
            # {'skupnopiškotki': [52], 'vlade': [21], 'spletnega': [86, 132], 'pregrada': [114], ...}
            # save to DB
            # word spletnega
            # frequency 2
            # indexes "86,132"
            # document name variable f

            break
        pass


if __name__ == "__main__":
    index = Index()
    index.populate_database()

