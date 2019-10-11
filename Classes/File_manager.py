from Classes.Dict_manager import File_info
from Classes.Path_manager import Path_info
import pandas as pd
from mutagen.easyid3 import EasyID3
import os

class File_tags:

    def __init__(self):

        self.path_original_file = None
        self.path_format_file = None
        self.path_clear_file = None
        self.which_version = None

        self.tags_content = None

        file_info = File_info()
        self.header_file_list = file_info.header_file_list

        self.path_info = Path_info()
        self.path_info.make_internal_dictionary(mkdir=False)

        self.path_data_original = self.path_info.path_data_original
        self.path_data_format = self.path_info.path_data_format
        self.path_data_clear = self.path_info.path_data_clear
        self.path_dictionary = self.path_info.path_dictionary

        self.list_genre = self.path_info.list_genre

        dict = {}
        directory_version_list = self.path_info.directory_version_list

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

    def reset(self):

        self.path_info.delete_format()
        self.path_info.make_directory()

    def tags_clear(self):

        tags = EasyID3(self.path_original_file)
        tags.save(self.path_clear_file)

    def tags_construct(self):

        tags = EasyID3(self.path_clear_file)
        for tag in self.header_file_list[2:]:
            tags[tag] = self.tags_content[tag]
        tags.save(self.path_format_file)

    def loop_tags_clear(self):

        for genre in self.list_genre:

            self.dictionary = pd.read_csv(self.path_dictionary + self.which_version + '//' + genre + '.csv',
                                          index_col=self.header_file_list[0])
            files_name = self.dictionary[self.header_file_list[1]]

            for file_name in files_name:

                try:

                    self.path_original_file = self.path_data_original + genre + '//' + file_name
                    self.path_clear_file = self.path_data_clear + genre + '//' + file_name

                    self.tags_clear()

                except:
                    print('{} is not exist. '.format(file_name))
                    pass

    def loop_tags_construct(self):

        for genre in self.list_genre:

            self.dictionary = pd.read_csv(self.path_dictionary + self.which_version + '//' + genre + '.csv')

            for i in range(self.dictionary.shape[0]):

                self.tags_content = self.dictionary.iloc[i]
                file_name = self.tags_content[self.header_file_list[1]]

                try:

                    self.path_clear_file = self.path_data_clear + genre + '//' + file_name
                    self.path_original_file = self.path_data_format + genre + '//' + file_name

                    self.tags_construct()

                except:
                    print('{} is not exist. '.format(file_name))
                    pass

    def read_file_info_csv(self):

        for genre in self.list_genre:

            df = pd.read_csv(self.path)
