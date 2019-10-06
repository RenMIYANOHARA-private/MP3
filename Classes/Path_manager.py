import os
import glob
import pandas as pd
import shutil

class Path_info:

    def __init__(self):

        self.sound_data_type = ['mp3']
        self.list_tags_target = [ 'lyricist', 'length', 'media', 'mood', 'title']

        self.header_original_files_edit = ['original', 'edited']

        self.path_abs = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        self.path_data_original = self.path_abs + '//Data Original//'
        self.path_data_format = self.path_abs + '//Data Format//'
        self.path_dictionary = self.path_abs + '//Dictionary//'

        self.list_genre = [os.path.basename(i) for i in os.listdir(self.path_data_original)]
        print(self.list_genre)

        if not os.path.exists(self.path_data_original):
            os.mkdir(self.path_data_original)
        if not os.path.exists(self.path_data_format):
            os.mkdir(self.path_data_format)
        if not os.path.exists(self.path_dictionary):
            os.mkdir(self.path_dictionary)
        for genre in self.list_genre:
            if not os.path.exists(self.path_data_format + genre):
                os.mkdir(self.path_data_format + genre)
            if not os.path.exists(self.path_dictionary + genre):
                os.mkdir(self.path_dictionary + genre)

    def delete_format(self):

        if os.path.exists(self.path_data_format):
            shutil.rmtree(self.path_data_format)

    def delete_dictionary(self):

        if os.path.exists(self.path_dictionary):
            shutil.rmtree(self.path_dictionary)

    def dictionary(self):

        for genre in self.list_genre:

            self.list_sound_files = [os.path.basename(i) for i in glob.glob(self.path_data_original + genre + '/*.mp3')]

            list_sound_files = pd.DataFrame(self.list_sound_files)

            list_sound_files.to_csv(self.path_dictionary + '{}.csv'.format(genre))
            print(self.path_data_original + '{}.csv'.format(genre) + 'list')



self = Path_info()
self.dictionary()

