from pydub import AudioSegment
import os
from pytube import YouTube

def download_audio(url, download_path):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(output_path=download_path)
    return audio_path

def clip_audio(input_path, output_path, clip_duration=10):
    audio = AudioSegment.from_file(input_path)
    clipped_audio = audio[:clip_duration * 1000]
    clipped_audio.export(output_path, format="mp3")
    
def merge_audios(clipped_files, output_path):
    if not clipped_files:
        print("No clipped files to merge")
        return
    
    combined = AudioSegment.from_file(clipped_files[0])
    
    for file in clipped_files:
        clip = AudioSegment.from_file(file)
        combined += clip
    combined.export(output_path, format="mp3")