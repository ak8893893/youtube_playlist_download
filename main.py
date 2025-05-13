from lib.download.download_youtube_playlist import download_youtube_playlist


"""
Title : YoutubePlayList 下載器新版 使用 yt-dlp
Author : AK
Time : 2025/5/13
"""


if __name__ == '__main__':
    playlist_url = input("請入輸入要下載的播放清單網址: ")  # 放入你的撥放清單網址
    downloadPath = "downloads"  # 輸入下載後的檔案要存放的位置

    media_type = input('要下載音樂或是影片？ 音樂請輸入 1 ，影片請輸入 2: ')
    if media_type == '1':
        download_type = 'audio'
    else:
        download_type = 'video'

    # 下載整個播放清單的音訊
    download_youtube_playlist(
        playlist_url = playlist_url,
        download_type = download_type,  # 使用'audio'下載MP3, 使用'video'下載影片
        output_path = downloadPath
    )

    print(f'下載完成 已將下載資料放到 {downloadPath} 資料夾中')
    exit_progress = input("下載程序執行完成   按下 enter 離開")