from Classes.Dict_manager import File_info
from Classes.Path_manager import Path_info
import pandas as pd
import os

class File_tags:

    def __init__(self):

        file_info = File_info()
        self.header_file_list = file_info.header_file_list


        path_info = Path_info()
        path_info.make_internal_dictionary(mkdir=False)


        self.path_data_original = path_info.path_data_original
        self.path_data_format = path_info.path_data_format
        self.path_dictionary = path_info.path_dictionary

        self.list_genre = path_info.list_genre

        dict = {}
        directory_version_list = path_info.directory_version_list

        for version in directory_version_list:

            genres_list = [os.path.basename(i) for i in os.listdir(self.path_dictionary + version + '//')]
            n_filesname = []

            for genre in genres_list:

                df = pd.read_csv(self.path_dictionary + version + '//' + genre)
                filesname = df[self.header_file_list[0]]
                n_filesname = n_filesname + [len(filesname)]

            dict[version] = [i for i in zip(genres_list, n_filesname)]

        for key, value in dict.items():

            print(key, ' : ', value)

    def read_file_info_csv(self):

        for genre in self.list_genre:

            df = pd.read_csv(self.path)