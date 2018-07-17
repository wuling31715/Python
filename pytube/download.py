from pytube import YouTube

def download():
    print('video links:')
    video = input()
    print('downloading...')
    path = 'datasets/mp4/'
    YouTube(video).streams.first().download(path)

download()