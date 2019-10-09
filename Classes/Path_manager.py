import os
import glob
import pandas as pd
import shutil

class Path_info:

    def __init__(self):

        self.header_original_files_edit = ['original', 'edited']
        self.path_abs = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.path_data_original = self.path_abs + '//Data Original//'
        self.path_data_format = self.path_abs + '//Data Format//'
        self.path_dictionary = self.path_abs + '//Dictionary//'

        self.list_genre = [os.path.basename(i) for i in os.listdir(self.path_data_original)]

        self.n_dictionary_version = 0

    def make_directory(self):

        if not os.path.exists(self.path_data_original):
            os.mkdir(self.path_data_original)
        if not os.path.exists(self.path_data_format):
            os.mkdir(self.path_data_format)
        if not os.path.exists(self.path_dictionary):
            os.mkdir(self.path_dictionary)

        for genre in self.list_genre:
            if not os.path.exists(self.path_data_format + genre):
                os.mkdir(self.path_data_format + genre)

    def make_internal_dictionary(self, mkdir=True):

        self.directory_version_list = [os.path.basename(i) for i in os.listdir(self.path_dictionary)]
        self.n_dictionary_version = len(self.directory_version_list)
        print('There are {} folder (num of version) in dictionary.'.format(self.n_dictionary_version))

        self.path_dictionary_version = self.path_dictionary + 'v{}//'.format(self.n_dictionary_version + 1)
        self.path_dictionary_pre_version = self.path_dictionary + 'v{}//'.format(self.n_dictionary_version)

        if mkdir:
            if not os.path.exists(self.path_dictionary_version):
                os.mkdir(self.path_dictionary_version)

    def delete_format(self):

        if os.path.exists(self.path_data_format):
            shutil.rmtree(self.path_data_format)

    def delete_dictionary(self):

        if os.path.exists(self.path_dictionary):
            shutil.rmtree(self.path_dictionary)

