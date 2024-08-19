import re
import os

def remove_prefix_suffix(filename, prefix_pattern, suffix_pattern):
    # Удаляем префикс
    filename = re.sub(f'^{prefix_pattern}', '', filename)
    # Удаляем суффикс
    filename = re.sub(f'{suffix_pattern}$', '', filename)
    return filename

def process_files_in_directory(directory, prefix_pattern, suffix_pattern):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = remove_prefix_suffix(filename, prefix_pattern, suffix_pattern)
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Старое имя файла: {filename} -> Новое имя файла: {new_filename}')

# Пример использования
directory = '.'  # Текущая директория
prefix_pattern = r'_.*?_.*?_'
suffix_pattern = r'\.png'

process_files_in_directory(directory, prefix_pattern, suffix_pattern)
