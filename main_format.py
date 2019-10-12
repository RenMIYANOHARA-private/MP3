from Classes.File_manager import File_tags

if __name__ == '__main__':

    file_tags = File_tags()

    file_tags.reset()
    file_tags.which_version = 'v2'
    file_tags.loop_tags_clear()

    file_tags.loop_tags_construct()
