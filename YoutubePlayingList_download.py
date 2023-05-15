"""
Title : YoutubePlayingList 下載器
Author : AK
Time : 2023/5/15
"""
from pytube import YouTube
from pytube import Playlist

url = input("請入輸入要下載的播放清單網址: ")                                    # 放入你的撥放清單網址
downloadPath = "download"                                                    # 輸入下載後的檔案要存放的位置

playlist = Playlist(url)
videolist = playlist.video_urls
pathdir = downloadPath                                                       # 下載後的檔案要存放的位置
print("總共有 " + str(len(videolist))+ " 部影片進入下載清單中")
print("-----------------下載開始---------------------------")
count=0
for video in videolist:

    yt = YouTube(video)
    print("正在下載影片: " + yt.title )
    yt.streams.filter(subtype='mp4', res='720p', progressive=True).first().download(pathdir)
    count+=1
    print(yt.title + " 下載完成 ")
    print("-----------------總下載進度" + str(count) + "/" + str(len(videolist)) + "---------------------")

exit_progress = input("下載程序執行完成   按下 enter 離開")