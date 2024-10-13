import argparse
import os
from src.youtube_scraper import get_songs_urls
from src.audio_processor import download_audio, clip_audio, merge_audios
from src.sendEmail import send_email

def main(singer, num_songs, clip_duration, output_file, recipient_mail):
    download_path = os.path.abspath("downloads")
    clipped_path = os.path.abspath("clipped")
    os.makedirs(download_path, exist_ok=True)
    os.makedirs(clipped_path, exist_ok=True)
    
    # Fetching song urls
    song_urls = get_songs_urls(singer, num_songs)
    clipped_files = []
    
    # download and clip each song
    for i, url in enumerate(song_urls):
        try:
            print(f"Downloading song {i+1}/{num_songs} from URL:{url}")
            audio_path = download_audio(url, download_path)
            clip_output_path = os.path.join(clipped_path, f"clip_{i+1}.mp3")
            clip_audio(audio_path, clip_output_path, clip_duration)
            clipped_files.append(clip_output_path)
        except Exception as e:
            print(f"Error processing song {i+1}: {e}")
            
    # Merging clipped files
    try:
        merge_audios(clipped_files, output_file)
        print(f"Compilation complete. File saved as {output_file}")
    except Exception as e:
        print(f"Error during merging: {e}")
        
    # Sending email
    if os.path.exists(output_file):
        send_email(output_file, recipient_mail)
    else:
        print(f"File not found: {output_file}. Cannot send email.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and clip songs from YouTube.")
    parser.add_argument('singer', type=str, help="Name of the singer")
    parser.add_argument('num_songs', type=int, help="number of songs")
    parser.add_argument('--clip-duration', type=int, default=10, help="Duration of each clip in seconds (default:10).")
    parser.add_argument('--output-file', type=str, default="final_output.mp3", help="Name of the final output file (final_output.mp3)")
    parser.add_argument('email_id', type=str, help="Where would you like to recieve email")
    
    args = parser.parse_args()
    
    main(args.singer, args.num_songs, args.clip_duration, args.output_file, args.email_id)