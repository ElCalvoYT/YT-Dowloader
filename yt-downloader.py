import yt_dlp
import os
import sys

def download_youtube_video(url, output_dir):
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Save the video with its title as the filename
        'format': 'best'  # Download the best quality video available
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Download complete! Video saved to {output_dir}")
    except Exception as e:
        print(f"Error: Failed to download the video. {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python yt_downloader.py <YouTube URL> <Output Directory>")
        sys.exit(1)

    video_url = sys.argv[1]
    save_dir = sys.argv[2]

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    download_youtube_video(video_url, save_dir)
