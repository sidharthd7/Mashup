import yt_dlp

def get_songs_urls(singer, n):
    search_query = f"{singer} official audio"
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': 'in_playlist',
        'default_search': 'ytsearch{}'.format(n),
        'skip_download': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download = False)
        songs = info['entries'][:n]
        song_urls = [song['url'] for song in songs]
    
    return song_urls