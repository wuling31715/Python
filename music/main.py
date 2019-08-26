from pydub import AudioSegment

def second_to_million_second(minute, second):
    return (60 * minute + second) * 1000

def main():
    file_name = 'Unbeatable Main Theme'
    file_path = 'input/%s.mp3' % file_name
    start_min = 0
    start_sec = 0
    end_min = 6
    end_sec = 45
    start_time = second_to_million_second(start_min, start_sec)
    end_time = second_to_million_second(end_min, end_sec)
    mp3 = AudioSegment.from_mp3(file_path)
    extract = mp3[:end_time]
    print('extracting...')
    export_path = 'output/%s.mp3' % file_name
    extract.export(export_path, format='mp3')
    print('exporting...')
    print('done.')

if __name__ == "__main__":
    main()