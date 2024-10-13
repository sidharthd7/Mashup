from pydub import AudioSegment
import os
import yt_dlp

def download_audio(url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        audio_path = ydl.prepare_filename(info_dict).replace('.webm', '.mp3')
    
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