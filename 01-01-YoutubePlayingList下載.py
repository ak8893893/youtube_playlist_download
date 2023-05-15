from pytube import YouTube
from pytube import Playlist
playlist = Playlist("網址")
videolist = playlist.video_urls
pathdir = 'download'  # 下載資料夾
for video in videolist:
    yt = YouTube(video)
    yt.streams.filter(subtype='mp4', res='720p', progressive=True).first().download(pathdir)