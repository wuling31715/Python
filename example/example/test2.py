from __future__ import unicode_literals
import youtube_dl
url = 'http://cn.vjav.com/videos/13514/old-man-next-door/'

ydl_opts = {
    'outtmpl': '/Volumes/space/download/%(title)s.%(ext)s',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
