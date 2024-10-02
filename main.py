import os

def copy_file_names_to_txt(folder_path, output_file):
    with open(output_file, 'w') as f:
        for file_name in os.listdir(folder_path):
            f.write(file_name + '\n')

folder_path = r"your directory here"
output_file = 'file_names.txt'

copy_file_names_to_txt(folder_path, output_file)
