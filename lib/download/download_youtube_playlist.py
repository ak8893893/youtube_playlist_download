import yt_dlp

def download_youtube_playlist(playlist_url, download_type='audio', output_path=None, start_from = 0):
    """
    下載YouTube播放清單中的所有影片/音訊（盡量以最高畫質/音質抓取）
    """
    try:
        # 基本與通用選項
        ydl_opts = {
            'ignoreerrors': True,               # 單支影片失敗不影響整清單
            'nocheckcertificate': True,
            # 'noplaylist': False,                # 下載整個播放清單
            'continuedl': True,                 # 斷點續傳
            'retries': 10,                      # 網路/HTTP 重試
            'fragment_retries': 10,
            'concurrent_fragment_downloads': 5, # 分段並行下載（提升速率）
            'trim_file_name': 240,              # 避免檔名過長
            # 'restrictfilenames': True,          # 檔名只用安全字元（特別是 Windows）
            # 'windowsfilenames': True,
            # 'writethumbnail': False,            # 需要縮圖時可設 True
            'cookiefile': 'cookies.txt',        # 載入手動匯出的cookies
        }

        # 判斷是不是播放清單
        is_playlist = "list=" in playlist_url and "watch?v=" not in playlist_url

        if is_playlist:
            ydl_opts['noplaylist'] = False  # 下載整個播放清單
            if start_from > 0:
                ydl_opts['playliststart'] = start_from
        else:
            ydl_opts['noplaylist'] = True   # 單一影片只下載該影片

        if start_from !=0:
            ydl_opts.update({
                'playliststart': start_from
            })

        # 檔名模板
        if output_path:
            if is_playlist:
                ydl_opts['outtmpl'] = f'{output_path}/%(playlist)s/%(playlist_index)s-%(title)s.%(ext)s'
            else:
                ydl_opts['outtmpl'] = f'{output_path}/%(title)s.%(ext)s'
        else:
            ydl_opts['outtmpl'] = '%(title)s.%(ext)s'

        if download_type.lower() == 'audio':
            # 僅音訊：抓 bestaudio，轉成 mp3（避免 re-encode 可改存原格式：移除 postprocessors）
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            # 影片：明確選「最佳影片軌 + 最佳音訊軌」，限制在 4320p / 60fps 以內（避免誤選更高規格）
            # 備援：若無分離軌，退而求其次抓單一 best
            ydl_opts.update({
                'format': (
                    'bestvideo[height<=?4320][fps<=?60]+bestaudio/'
                    'best[height<=?4320][fps<=?60]'
                ),
                'merge_output_format': 'mkv',

                # 正確的排序寫法
                'format_sort': [
                    'height:desc',  # 高解析度優先
                    'fps:desc',  # 高幀率優先
                    'vcodec:av01',  # 偏好 AV1（可依需求改）
                    'vcodec:vp9',
                    'vcodec:h264',
                    'acodec:opus',
                    'filesize:desc'  # 檔案大小大優先（通常代表品質好）
                ],
                'format_sort_force': True,  # 強制依照這個排序
            })

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=False)
            if 'entries' in info:  # 播放清單
                title = info.get('title', 'Unknown Playlist')
                videos = [e for e in info['entries'] if e]
                print(f"開始下載播放清單: {title}, 共 {len(videos)} 個影片")
            else:  # 單一影片
                title = info.get('title', 'Unknown Video')
                print(f"開始下載單一影片: {title}")

            ydl.download([playlist_url])
            print("下載完成！")
            return True

    except Exception as e:
        print(f"下載失敗: {e}")
        return False


if __name__ == "__main__":
    # 1. 播放清單
    # playlist_url = "https://www.youtube.com/playlist?list=PLjJlRS13Ym5R1k_X8lFA1SKpxZPwXcjfw"
    # 2. 單一影片
    playlist_url = "https://www.youtube.com/watch?v=6e82HzMK_qI&t=5s"

    start_from = 0

    download_youtube_playlist(
        playlist_url=playlist_url,
        download_type='video',   # 'audio' 下載 MP3；'video' 下載最高畫質影片
        output_path="downloads",
        start_from = start_from
    )
