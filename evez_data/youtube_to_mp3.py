```python
import argparse
import os
import subprocess
import sys
from urllib.parse import urlparse

def main():
    parser = argparse.ArgumentParser(description="YouTube to MP3 converter")
    parser.add_argument("url", help="YouTube video URL")
    args = parser.parse_args()

    music_dir = os.path.expanduser("~/Music")
    os.makedirs(music_dir, exist_ok=True)

    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--progress",
        "--no-playlist",
        "-o", os.path.join(music_dir, "%(title)s.%(ext)s"),
        args.url
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("yt-dlp not found. Install with: sudo apt install yt-dlp", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```