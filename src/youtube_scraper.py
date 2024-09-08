from pytube import Search

def get_songs_urls(singer, n):
    search_query = f"{singer} official audio"
    search = Search(search_query)
    songs = search.results[:n]
    song_urls = [song.watch_url for song in songs]
    return song_urls