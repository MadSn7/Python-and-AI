# from pytube import YouTube
# from pytube.exceptions import VideoUnavailable, RegexMatchError, LiveStreamError

# def download_video_1080p(url):
#     """
#     Downloads a YouTube video in 1080p resolution.
    
#     Args:
#         url (str): The URL of the YouTube video.
#     """
#     try:
#         # Create a YouTube object from the URL
#         yt = YouTube(url)
        
#         print(f"Video Title: {yt.title}")
        
#         # Filter for the 1080p progressive stream
#         # Progressive streams have both video and audio in a single file
#         stream = yt.streams.filter(res="1080p", progressive=True).first()

#         # Check if the 1080p stream was found
#         if stream:
#             print("1080p stream found. Downloading...")
#             stream.download()
#             print("Download completed successfully!")
#         else:
#             # If the stream is not found, raise an error
#             print("Error: 1080p video stream not found.")
#             print("Available resolutions:")
#             # List all available progressive streams for debugging
#             available_streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
#             for s in available_streams:
#                 print(f"  - {s.resolution}")
#             raise FileNotFoundError("1080p resolution not available for this video.")

#     except RegexMatchError:
#         print("Error: The URL provided is not a valid YouTube video URL.")
#     except VideoUnavailable:
#         print("Error: The video is unavailable or has restrictions.")
#     except LiveStreamError:
#         print("Error: Cannot download live streams.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     # Example usage:
#     video_url = "https://www.youtube.com/watch?v=y6n5bvXcMhY"
#     print("Starting download...")
#     # You can replace the URL with the video you want to download.
#     # To test the error case, you can use a video that doesn't have 1080p.
#     # For example, a video with a max resolution of 720p.
#     # Replace 'your_video_id_here' with the actual video ID.
    
#     download_video_1080p(video_url)

import subprocess
import json
import re

def download_video_1080p_ytdlp(url):
    """
    Downloads a YouTube video in 1080p resolution using yt-dlp.
    
    Args:
        url (str): The URL of the YouTube video.
    """
    print("Fetching video information...")
    
    # First, use yt-dlp to get video information in JSON format
    try:
        command = ['yt-dlp', '--dump-single-json', url]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        video_info = json.loads(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"Error fetching video info: {e.stderr}")
        if "ERROR: [youtube] " in e.stderr:
            # Check for common YouTube-specific errors
            error_message = re.search(r"ERROR: \[youtube\] (.*)", e.stderr)
            if error_message:
                print(f"Error: {error_message.group(1).strip()}")
            else:
                print("Error: Could not retrieve video information. It may be unavailable or private.")
        return
    except json.JSONDecodeError:
        print("Error: Could not parse video information. The video may be restricted or the URL is invalid.")
        return
    except FileNotFoundError:
        print("Error: yt-dlp is not installed or not in your system's PATH.")
        print("Please install it by following the instructions at: https://github.com/yt-dlp/yt-dlp")
        return

    # Extract the video title
    video_title = video_info.get('title', 'Untitled Video')
    print(f"Video Title: {video_title}")

    # Find the best 1080p format that includes both video and audio
    format_code = None
    formats = video_info.get('formats', [])
    for fmt in formats:
        # Look for a progressive stream with 1080p resolution
        if 'resolution' in fmt and fmt['resolution'] == '1080p' and fmt.get('ext') == 'mp4' and fmt.get('acodec') != 'none':
            format_code = fmt.get('format_id')
            break
    
    if format_code:
        print("1080p stream found. Downloading...")
        try:
            # Command to download the specific format
            download_command = ['yt-dlp', '-f', format_code, url]
            subprocess.run(download_command, check=True)
            print("Download completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading video: {e.stderr}")
    else:
        print("Error: 1080p video stream not found.")
        print("Available progressive resolutions:")
        # List all available progressive streams
        for fmt in formats:
            if fmt.get('acodec') != 'none' and fmt.get('vcodec') != 'none':
                print(f"  - {fmt.get('resolution')}")
        print("\nNote: For 1080p and higher, video and audio are often separate streams.")
        print("To download and merge them, you need to have FFmpeg installed.")
        print("FFmpeg can be downloaded from: https://ffmpeg.org/download.html")

if __name__ == "__main__":
    # Example usage:
    video_url = "https://www.youtube.com/watch?v=y6n5bvXcMhY"
    
    # Replace with a video URL of your choice.
    download_video_1080p_ytdlp(video_url)