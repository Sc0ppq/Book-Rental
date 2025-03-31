import shutil

def copy_file_content(source_file, destination_file):
    shutil.copyfile(source_file, destination_file)

def clear_file_content(filename):
    with open(filename, 'w') as f:
        pass