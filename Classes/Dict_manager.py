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

        path_info = Path_info()

        self.mode = mode

        self.header_file_list = ['#  ', 'name', 'title']
        self.list_tags_target = ['lyricist', 'length', 'media', 'mood', 'title']
        self.kinds_of_file = ['mp3', 'aac', 'wma', 'wav']

        self.path_data_original = path_info.path_data_original
        self.path_dictionary = path_info.path_dictionary

        self.genre = None
        self.list_genre = path_info.list_genre

        path_info.make_directory()
        path_info.make_internal_dictionary(mkdir=True)
        self.n_dictionary_version = path_info.n_dictionary_version
        self.path_dictionary_version = path_info.path_dictionary_version
        self.path_dictionary_pre_version = path_info.path_dictionary_pre_version

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

            data = pd.read_csv(self.path_dictionary_pre_version + '{}.csv'.format(self.genre))
            pre_files_name = data[self.header_file_list[1]]

            self.n_pre_files = len(pre_files_name)
            print(self.n_pre_files)

            for pre_file in pre_files_name:

                try:

                    self.files_name.remove(pre_file)

                except:

                    print('{} is not exist in Original directory. '.format(pre_file))

            print('New files >>> ')
            for file in self.files_name:
                print('             ', file)

    def dictionary_genre(self):

        if self.mode == 'w':

            self.header_file_list = np.array(self.header_file_list)

            header_file_list = pd.DataFrame(self.header_file_list[np.newaxis, :])
            files_name = pd.DataFrame(self.files_name)

            header_file_list.to_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                                    mode='w', header=False, index=False, encoding='utf-8')
            files_name.to_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                              mode='a', header=False, encoding='utf-8')

            print('List ' + self.path_dictionary_version + '{}.csv'.format(self.genre))

        if self.mode == 'a':


            shutil.copy(self.path_dictionary_pre_version + '{}.csv'.format(self.genre),
                        self.path_dictionary_version)

            pre_files_name = pd.read_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                                         index_col=self.header_file_list[0])

            files_name = pd.DataFrame(self.files_name)
            files_name.set_index(pd.Index([i for i in range(self.n_pre_files, self.n_pre_files + len(files_name))]))

            files_name.to_csv(self.path_dictionary_version + '{}.csv'.format(self.genre),
                              mode='a', header=False, encoding='utf-8')




