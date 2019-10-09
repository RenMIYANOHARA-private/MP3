from Classes.Path_manager import Path_info
from Classes.Dict_manager import File_info

if __name__ == '__main__':

    file_info = File_info()

    list_genre = file_info.list_genre
    file_info.set_specific_version()

    for genre in list_genre:

        file_info.genre = genre
        file_info.gather_all_type_file()
        file_info.check_previous_version()
        file_info.dictionary_genre()

