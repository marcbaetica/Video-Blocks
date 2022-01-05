import os
from lib.video_editor_tools import split_mp4_to_jgp


INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

for file in os.listdir(INPUT_FOLDER):
    if '.mp4' in file:
        print(f'Found video {file}. Splitting to frames:')
        frames_output_folder = f'{OUTPUT_FOLDER}/{file.split(".")[0]}'
        os.mkdir(frames_output_folder)
        split_mp4_to_jgp(f'{INPUT_FOLDER}/{file}', frames_output_folder)
