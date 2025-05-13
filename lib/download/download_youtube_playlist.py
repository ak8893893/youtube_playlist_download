import yt_dlp


def download_youtube_playlist(playlist_url, download_type='audio', output_path=None):
    """
    下載YouTube播放清單中的所有影片

    參數:
        playlist_url (str): YouTube播放清單的URL
        download_type (str): 'audio'僅下載音訊, 'video'下載影片
        output_path (str, optional): 輸出路徑

    返回:
        bool: 下載是否成功
    """
    try:
        # 基本選項
        ydl_opts = {
            'ignoreerrors': True,  # 跳過錯誤的影片繼續下載其他
            'nocheckcertificate': True,
            'noplaylist': False,  # 必須為False才能下載整個播放清單
        }

        # 輸出路徑和檔名格式設定
        if output_path:
            # 播放清單格式化: 資料夾名稱為播放清單標題, 檔案名包含編號和標題
            ydl_opts['outtmpl'] = f'{output_path}/%(playlist)s/%(playlist_index)s-%(title)s.%(ext)s'
        else:
            ydl_opts['outtmpl'] = '%(playlist)s/%(playlist_index)s-%(title)s.%(ext)s'

        # 根據下載類型設定不同選項
        if download_type.lower() == 'audio':
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:  # 視頻模式
            ydl_opts.update({
                'format': 'best',  # 最佳品質的視頻+音訊
            })

        # 執行下載
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 先獲取播放清單資訊
            info_dict = ydl.extract_info(playlist_url, download=False)

            if 'entries' in info_dict:
                # 顯示播放清單資訊
                playlist_title = info_dict.get('title', 'Unknown Playlist')
                video_count = len(info_dict['entries'])
                print(f"開始下載播放清單: {playlist_title}")
                print(f"共有 {video_count} 個影片需要下載")

                # 執行實際下載
                ydl.download([playlist_url])

                print(f"播放清單 '{playlist_title}' 下載完成！")
                return True
            else:
                print("無法獲取播放清單資訊")
                return False

    except Exception as e:
        print(f"下載失敗: {e}")
        return False


# 使用範例
if __name__ == "__main__":
    # 請替換為您想下載的YouTube播放清單URL
    playlist_url = "https://www.youtube.com/playlist?list=PLjJlRS13Ym5R1k_X8lFA1SKpxZPwXcjfw"

    # 下載整個播放清單的音訊
    download_youtube_playlist(
        playlist_url=playlist_url,
        download_type='video',  # 使用'audio'下載MP3, 使用'video'下載影片
        output_path="downloads"
    )