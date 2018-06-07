# from __future__ import unicode_literals
# import uniout
import youtube_dl


def mp4_download(url):
    ydl_opts = {
        'outtmpl': '/Volumes/space/download/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def mp3_download(url):
    ydl_opts = {
        'outtmpl':
        '/Volumes/space/download/%(title)s.%(ext)s',
        'format':
        'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def both_download(url):
    mp3_download(url)
    mp4_download(url)

#mp3_download('')
mp4_download('https://www.thisav.com/video/embed/138117/')
#both_download('')