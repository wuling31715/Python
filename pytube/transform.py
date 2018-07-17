import ffmpeg
import os

def transform(file):
    file_list = file.split('.')
    if file_list[1] == 'mp4':
        file_name = file_list[0]
        path = 'datasets/mp4/' + file 
        stream = ffmpeg.input(path)
        path = 'datasets/mp3/' + file_name + '.mp3'
        stream = ffmpeg.output(stream, path)
        print('transforming...')
        ffmpeg.run(stream)

path = 'datasets/mp4/'
for file in os.listdir(path):
    transform(file)
    print('done.')