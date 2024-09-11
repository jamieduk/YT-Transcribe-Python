#
# (c) J~Net 2024

# https://jnet.forumotion.com/t2036-python-youtube-transcribe-function#3151
# pip install youtube-transcript-api
#
# python yt-transcript.py
#
#
import os
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url):
    """Extract the video ID from a YouTube URL."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_transcript(url):
    video_id=get_video_id(url)
    if not video_id:
        return "Invalid YouTube URL."
    
    try:
        transcript=YouTubeTranscriptApi.get_transcript(video_id)
        formatter=TextFormatter()
        formatted_transcript=formatter.format_transcript(transcript)
        return formatted_transcript
    except Exception as e:
        return f"An error occurred: {str(e)}"

def save_transcript(transcript):
    timestamp=time.strftime("%Y%m%d_%H%M%S")
    file_name=f"transcript_{timestamp}.txt"
    full_path=os.path.join(os.getcwd(), file_name)
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(transcript)
    return full_path

# Example usage
url=input("Enter the YouTube video URL: ")
transcript=fetch_transcript(url)

# Output the transcript to the console
print(transcript)

# Save the transcript to a file in the current working directory
full_path=save_transcript(transcript)
print(f"\nTranscript saved as {full_path}")

