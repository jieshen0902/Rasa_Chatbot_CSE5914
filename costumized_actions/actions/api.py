import json
from dotenv import load_dotenv
import os
import base64
from requests import post, get

load_dotenv()

# Set-up the client id and client secret
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


##################      Set-up token       ##################
# Get token and make it ready
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer "+token}



##################      Set-up Search api       ##################
# Set-up the search for artist api
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None

    return json_result[0]

# Set-up the search for song api
def search_for_song(token, song_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={song_name}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if len(json_result) == 0:
         print("No song with this name exists...")
         return None

    return json_result[0]

# Set-up the search for album api
def search_for_album(token, album):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={album}&type=album&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    #result.content
    json_result = json.loads(result.content)["albums"]["items"]
    if len(json_result) == 0:
        print("No song with this album exists...")
        return None

    return json_result[0]



##################      Set-up Artists api       ##################
# Artist to top track songs 
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

# Aritst to related artists
def get_artists_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["artists"]
    return json_result

# Aritst to albums
def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['items']
    return json_result



##################      Set-up Tracks api       ##################
# Get track feature
def get_track_features(token, song_id):
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result



##################      Set-up Album api       ################## 
# Album to songs in the album
def get_songs_by_album(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result






##################      Set-up searching method       ##################
# Search the top tracks
def search_songs_by_artist(token, artist_id):
    songs = get_songs_by_artist(token, artist_id)
    song_names = []
    for idx, song in enumerate(songs):
        song_names.append(f"{idx + 1}. {song['name']}")
    return song_names

# Search the related artists
def search_artists_by_artist(token, artist_id):
    artists = get_artists_by_artist(token, artist_id)
    artist_names = []
    for idx, artist in enumerate(artists):
        artist_names.append(f"{idx + 1}. {artist['name']}")
    return artist_names

# Search the albums by artist
def search_albums_by_artist(token, artist_id):
    albums = get_albums_by_artist(token, artist_id)
    album_names = []
    for idx, album in enumerate(albums):
        album_names.append(f"{idx + 1}. {album['name']}")
    return album_names



# Search the album by song
def search_albums_by_song(token, song_id):
    album = get_track_features(token, song_id)["album"]
    album_names = []
    album_names.append(album['name'])
    return album['name']

# Search the artists by song
def search_artists_by_song(token, song_id):
    artists = get_track_features(token, song_id)["artists"]
    artist_names = []
    for idx, artist in enumerate(artists):
        artist_names.append(f"{idx + 1}. {artist['name']}")
    return artist_names

# Search songs by album name
def search_songs_by_album(token, album_id):
    songs = get_songs_by_album(token, album_id)["items"]
    song_names = []
    for idx, song in enumerate(songs):
        song_names.append(f"{idx + 1}. {song['name']}")
    return song_names




##################      Main       ##################
token = get_token()

# Enter the artist
# artist_id = search_for_artist(token, "周杰伦")["id"]
# album_names = search_albums_by_artist(token, artist_id)
# for element in album_names:
#     print(element)

# search_songs_by_artist(token, artist_id)
# search_artists_by_artist(token, artist_id)

# Enter the song
# song_id = search_for_song(token, "晴天")["id"]
# search_artists_by_song(token, song_id)
# print(search_albums_by_song(token, song_id))

# Enter the album
# album_id = search_for_album(token, "24K Magic")["id"]
# song_names = search_songs_by_album(token, album_id)
# or element in song_names:
#    print(element)