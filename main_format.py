from Classes.Path_manager import Path_info
from Classes.Dict_manager import File_info
from Classes.File_manager import File_tags
import pandas as pd

if __name__ == '__main__':

    file_tags = File_tags()

    file_tags.reset()
    file_tags.which_version = 'v1'
    file_tags.loop_tags_clear()

    file_tags.loop_tags_construct()
