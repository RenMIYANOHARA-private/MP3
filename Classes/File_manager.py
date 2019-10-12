from Classes.Dict_manager import File_info
from Classes.Path_manager import Path_info
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TRCK, APIC, TDRC, TCON
from mutagen.mp3 import MP3
import mutagen.id3
import pandas as pd
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

        m = MP3(self.path_clear_file, ID3=ID3)
        m["TRCK"] = TRCK(encoding=3, text='')
        m["TIT2"] = TIT2(encoding=3, text='')
        m['TCON'] = TCON(encoding=3, text='')
        m["TPE1"] = TPE1(encoding=3, text='')
        m["TALB"] = TALB(encoding=3, text='')
        m['TDRC'] = TDRC(encoding=3, text='')
        m.save()

    def tags_construct(self):

        m = MP3(self.path_format_file, ID3=ID3)

        if self.tags_content['track']:
            m["TRCK"] = TRCK(encoding=3, text=str(self.tags_content['No']))

        if self.tags_content['title']:
            m["TIT2"] = TIT2(encoding=3, text=str(self.tags_content['title']))

        if self.tags_content['genre']:
            m['TCON'] = TCON(encoding=3, text=str(self.tags_content['genre']))

        if self.tags_content['artist']:
            m["TPE1"] = TPE1(encoding=3, text=str(self.tags_content['artist']))

        if self.tags_content['album']:
            m["TALB"] = TALB(encoding=3, text=str(self.tags_content['album']))

        if self.tags_content['date']:
            m['TDRC'] = TDRC(encoding=3, text=str(self.tags_content['date']))

        m.save()

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
                    self.path_format_file = self.path_data_format + genre + '//' + file_name

                    self.tags_construct()

                except:
                    print('{} is not exist. '.format(file_name))
                    pass

    def read_file_info_csv(self):

        for genre in self.list_genre:

            df = pd.read_csv(self.path)
