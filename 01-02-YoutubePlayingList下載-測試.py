"""
Title : YoutubePlayingList 下載器
Author : AK
Time : 2022/11/13
"""
from pytube import YouTube
from pytube import Playlist


url = ""                                    # 放入你的撥放清單網址
downloadPath = ""                           # 輸入下載後的檔案要存放的位置


playlist = Playlist(url)
videolist = playlist.video_urls
pathdir = downloadPath                      # 下載後的檔案要存放的位置
for video in videolist:
    yt = YouTube(video)
    yt.streams.filter(subtype='mp4', res='720p', progressive=True).first().download(pathdir)