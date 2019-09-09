import os
from pydub import AudioSegment

def second_to_million_second(minute, second):
    return (60 * minute + second) * 1000

def get_file():
    file_list = os.listdir('input')
    for file in file_list:
        if '.mp3' in file:
            return file
    
def main():
    file_name = get_file()
    file_path = 'input/%s' % file_name
    start_min = 0
    start_sec = 4
    end_min = 0
    end_sec = 0
    start_time = second_to_million_second(start_min, start_sec)
    end_time = second_to_million_second(end_min, end_sec)
    mp3 = AudioSegment.from_mp3(file_path)
    extract = mp3[start_time:]
    print('extracting %s...' % file_name)
    export_path = 'output/%s' % file_name
    extract.export(export_path, format='mp3')
    print('exporting %s...' % file_name)
    print('done.')

if __name__ == "__main__":
    main()