import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id = '7495d6c6f90b4c3d8a2d588945eec06b',
                                        client_secret = '4bef24996fb74ba78a4d698313965343')
sp = spotipy.Spotify(auth_manager=auth_manager)

class Artist():
    def __init__(self, spotify_uri):
        self.spotify_uri = spotify_uri
    def info(spotify_uri):
        artist_info = sp.artist(spotify_uri)
        return artist_info
    def tracks(spotify_uri):
        track_list = sp.album_tracks(spotify_uri)
        return track_list

class Playlist():
    def __init__(self, spotify_uri):
        self.spotify_uri = spotify_uri
    def info(spotify_uri):
        playlist_info = sp.playlist(spotify_uri)
        return playlist_info
        
class Display():
    def __init__(self, playlist):
        self.playlist = playlist
    def track_list(playlist):
        for track in playlist['items']:
            return track['name']
    def play_list(playlist):
        bingo_list = []
        for i in range(0,50):
            bingo_list.append(top_50['tracks']['items'][i]['track']['name'])
        return bingo_list

top_50 = Playlist.info('spotify:playlist:37i9dQZF1DXcBWIGoYBM5M')
for_bingo = Display.play_list(top_50)
