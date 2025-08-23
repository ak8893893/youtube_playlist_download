# Youtube Playlist Downloader (yt-dlp)

這是一個基於 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 的 Python 工具，用於下載 YouTube 播放清單或單一影片，支援最高畫質影片及音訊下載，並具備斷點續傳功能。

## 功能特色
- 支援 **整個播放清單** 或 **單一影片** 下載  
- 可選擇 **音樂 (MP3)** 或 **影片 (MKV)** 格式  
- 自動使用最高可用畫質/音質 (支援到 4320p/60fps)  
- 支援 **斷點續傳**，下載中斷可繼續  
- 可設定從播放清單的第幾個影片開始下載  
- 下載完成後自動依播放清單分類存檔  

## 專案結構
```
.
├── main.py                     # 主程式，提供互動式 CLI 輸入
├── download_youtube_playlist.py # 下載邏輯封裝
├── cookies.txt                 # (可選) 匯出的 YouTube cookies
└── downloads/                  # 預設下載資料夾
```

## 安裝需求
- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [ffmpeg](https://ffmpeg.org/) (轉換音訊格式需要)

安裝方式：
```bash
pip install yt-dlp
```

確認 `ffmpeg` 已安裝：
```bash
ffmpeg -version
```

## 使用方式

### 互動模式 (推薦)
直接執行 `main.py`：
```bash
python main.py
```
會提示輸入：
1. **播放清單或影片網址**  
2. **選擇下載音樂 (輸入 1) 或影片 (輸入 2)**  
3. **從第幾個影片開始下載**（0 表示從頭開始）

下載完成後檔案會存放在 `downloads/` 資料夾中。

## 參數說明
| 參數          | 說明 |
|---------------|------|
| `playlist_url` | YouTube 播放清單或單一影片連結 |
| `download_type` | `'audio'` 下載 MP3，`'video'` 下載影片 |
| `output_path` | 檔案下載的資料夾 (預設為當前目錄) |
| `start_from` | 從第幾個影片開始下載 (預設 `0` 表示從頭) |

## 注意事項
- 建議搭配 `cookies.txt` 使用，避免部分影片無法下載  
- `cookies.txt` 可透過瀏覽器外掛 (如 [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg)) 匯出
- 放入根目錄下的 cookie.txt 中
