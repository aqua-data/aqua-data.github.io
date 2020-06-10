import os
import random
import shutil
import sys


def sample_files():
    in_dir = sys.argv[1]
    source_dir = os.path.join(in_dir, "tabel")
    target_dir = os.path.join(in_dir, "tabel-sample")

    source_files = []
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.csv'):
            source_files.append(file_name)
    random.shuffle(source_files)

    for file_name in source_files[:1000]:
        file_id = file_name.split('.')[0]
        for ext in ['.csv', '.types', '.meta']:
            source_path = os.path.join(source_dir, '{}{}'.format(file_id, ext))
            target_path = os.path.join(target_dir, '{}{}'.format(file_id, ext))
            shutil.copyfile(source_path, target_path)
        

def move_files():
    in_dir = sys.argv[1]
    source_dir = os.path.join(in_dir, 'tabel')
    target_dir = os.path.join(in_dir, 'tabel-sample')

    for file_name in os.listdir(target_dir):
        if file_name.endswith('.csv') or file_name.endswith('.types') or file_name.endswith('.meta'):
            source_path = os.path.join(source_dir, file_name)
            target_path = os.path.join(target_dir, file_name)
            shutil.copyfile(source_path, target_path)


if __name__ == '__main__':
    # sample_files()
    move_files()
