# YouTube Downloader

## Project Description

A versatile YouTube downloader that uses yt-dlp to download videos or music from YouTube. This tool supports downloading both individual videos and entire playlists in either high-quality video or audio formats. The program automatically organizes downloads by playlist and maintains original quality while ensuring proper audio-video synchronization.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Configuration](#configuration)
5. [Examples](#examples)
6. [Build](#build)

## Installation

### Prerequisites

- Python 3.10+
- pip
- Git

### Installation Steps

1. Clone this repository:
    
```bash
git clone [your-repository-url]
cd youtube-downloader
```

2. Install required packages:
    
```bash
pip install -r requirements.txt
```

This will install the necessary dependencies:
- yt-dlp
- pytube (alternative downloader)

## Usage

Run the main script to start the downloader:

```bash
python main.py
```

The script will:
1. Prompt you to enter a YouTube URL (video or playlist)
2. Ask whether you want to download audio (MP3) or video (MP4)
3. Download the content to the specified output directory
4. Organize downloads by playlist name automatically

### Command Line Options

Alternatively, you can create your own script using the download module directly:

```python
from lib.download.download_youtube_playlist import download_youtube_playlist

# Download a playlist as audio
download_youtube_playlist(
    playlist_url="https://www.youtube.com/playlist?list=PLxxxxx",
    download_type='audio',  # Use 'audio' for MP3, 'video' for MP4
    output_path="downloads"
)
```

## Features

- **High-Quality Video Downloads**: Automatically selects the highest available video quality
- **Audio Extraction**: Converts videos to high-quality MP3 files
- **Playlist Support**: Downloads entire playlists while maintaining organization
- **Format Options**: Choose between video or audio-only downloads
- **Consistent Naming**: Organizes files with sequential numbering and original titles
- **Error Handling**: Skips problematic videos to ensure completion of playlist downloads
- **Progress Tracking**: Displays download progress and playlist information

## Configuration

The downloader automatically creates files with the following structure:

```
downloads/
└── [Playlist Name]/
    ├── 1-[Video Title].mp4
    ├── 2-[Video Title].mp4
    └── ...
```

For audio downloads, the structure is similar but with .mp3 files instead.

## Examples

### Downloading a Playlist as Audio

```python
download_youtube_playlist(
    playlist_url="https://www.youtube.com/playlist?list=PLxxxxx",
    download_type='audio',
    output_path="music"
)
```

### Downloading a Single Video in Highest Quality

```python
download_youtube_playlist(
    playlist_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    download_type='video',
    output_path="videos"
)
```

## Troubleshooting

### Common Issues

- **Video with No Sound**: If your downloaded videos lack audio, make sure you're using the latest version of the script, which handles audio-video merging properly.
- **Low Video Quality**: The downloader automatically selects the highest quality. If you're getting low quality, it may be the best available for that particular video.
- **Download Failures**: Some videos may be region-restricted or private. The downloader will skip these and continue with the rest of the playlist.

### Updating

YouTube occasionally changes its systems. To ensure compatibility, regularly update your dependencies:

```bash
pip install -U yt-dlp pytube
```

## Note

Please use this tool responsibly and respect copyright laws. This downloader should only be used for content you have permission to download or that falls under fair use.

## Build

If you want build a .exe file for windows, please follow the steps

1. Install all packages
```bash
pip install -r requirements.txt
```

2. Install pyinstaller 
```bash
pip install pyinstaller
```

3. Use pyinstaller to build the single exe file
```bash
pyinstaller -F main.py
```

4. The file will be at the dist folder. e.g. `main.exe`
