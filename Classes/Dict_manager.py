from Classes.Path_manager import Path_info
import os
import glob
import pandas as pd
import numpy as np
import shutil

class File_info:

    def __init__(self, mode='a'):
        """
        mode = 'a' >>> Update only new files.
        mode = 'w' >>> Update all files.
        """

        self.path_info = Path_info()

        self.mode = mode

        self.header_file_list = ['No', 'name', 'title', 'genre', 'artist', 'album', 'date']
        self.list_tags_target = ['lyricist', 'length', 'media', 'mood', 'title']
        self.kinds_of_file = ['mp3', 'aac', 'wma', 'wav']

        self.path_data_original = self.path_info.path_data_original
        self.path_dictionary = self.path_info.path_dictionary

        self.genre = None
        self.list_genre = self.path_info.list_genre

    def set_specific_version(self):

        self.path_info.make_directory()
        self.path_info.make_internal_dictionary(mkdir=True)
        self.n_dictionary_version = self.path_info.n_dictionary_version
        self.path_dictionary_version = self.path_info.path_dictionary_version
        self.path_dictionary_pre_version = self.path_info.path_dictionary_pre_version

    def gather_all_type_file(self):

        self.files_name = []

        for k in self.kinds_of_file:

            self.files_name = self.files_name + [os.path.basename(i) for i in glob.glob(self.path_data_original +
                                                                                        self.genre + '/*.{}'.format(k))]


    def check_previous_version(self):

        if self.n_dictionary_version == 0:

            self.mode = 'w'
            print('There is no data in dictionary directory. ')

        else:
            try:

                data = pd.read_csv(self.path_dictionary_pre_version + '{}.csv'.format(self.genre), encoding='cp932')
                pre_files_name = data[self.header_file_list[1]]

                self.n_pre_files = len(pre_files_name)

                for pre_file in pre_files_name:

                    try:
                        self.files_name.remove(pre_file)

                    except:
                        print('{} is not exist in Original directory. '.format(pre_file))

            except:

                self.mode = 'w'

            print('New {} files >>> '.format(self.genre))
            for file in self.files_name:
                print('                 ', file)

    def dictionary_genre(self):

        if self.mode == 'w':

            self.header_file_list = np.array(self.header_file_list)

            header_file_list = pd.DataFrame(self.header_file_list[np.newaxis, :])
            files_name = pd.DataFrame(self.files_name)

            header_file_list.to_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                                    mode='w', header=False, index=False, encoding='utf-8')
            files_name.to_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                              mode='a', header=False, encoding='shift_jis')

            print('List ' + self.path_dictionary_version + '{}.csv'.format(self.genre))

        if self.mode == 'a':


            shutil.copy(self.path_dictionary_pre_version + '{}.csv'.format(self.genre),
                        self.path_dictionary_version)

            files_name = pd.DataFrame(self.files_name)

            files_name.index = files_name.index + self.n_pre_files

            files_name.to_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                              mode='a', header=False, encoding='shift_jis')




