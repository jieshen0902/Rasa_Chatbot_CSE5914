import json

import os
import base64
from requests import post, get



# Set-up the client id and client secret
client_id = "f3e1f1f9e39c4cb693c29c71bb6e3bb5"
client_secret = "5e796b30ebaa4827913db426054b5b90"


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



##################      Set-up Basic api       ##################
# Set-up the search for artist api

# return a single dictionary element: contains (json_result[0] + ) image url(["images"][-1]["url"]), external url(["external_urls"]["spotify"]) and name (["name"])
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
        print("No album with this album exists...")
        return None

    return json_result[0]

# Set-up the search for playlist api
def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None

    return json_result[0]

# set-up the browse new-release api
def get_for_new_release_album(token):
   url = "https://api.spotify.com/v1/browse/new-releases"
   headers = get_auth_header(token)

   query_url = url
   result = get(query_url, headers=headers)

   json_result = json.loads(result.content)["albums"]
   if len(json_result) == 0:
       print("No newly release album...")
       return None
  
   return json_result

##################      Set-up Recommendation api       ##################
# set-up the recommendation api
def recommendation(token, artist_id, genres_name, song_id):
    url = "https://api.spotify.com/v1/recommendations"
    headers = get_auth_header(token)
    query = "?limit=5&market=us"

    if artist_id != "None":
        query += f"&seed_artists={artist_id}"
    if genres_name != "None":
        query += f"&seed_genres={genres_name}"
    if song_id != "None":
        query += f"&seed_tracks={song_id}"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    if len(json_result) == 0:
        print("No tracks found matching the given parameters...")
        return None

    return json_result


# Set-up the related_artist
def related_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = get_auth_header(token)

    query_url = url 
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None

    return json_result





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

##################      Set-up Playlist api       ################## 
# Get playlist feature
def get_playlist_features(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['items']
    return json_result





##################      Set-up searching method       ##################
## There are several types: songs,  artists, and album, where song dont have itself image, so use album image instead

# Search the top tracks
def search_songs_by_artist(token, artist_id):
    
    songs = get_songs_by_artist(token, artist_id)
    song_names = []
    e_url = []
    i_url = []
    
    for idx, song in enumerate(songs):
        song_names.append(song['name'])
        e_url.append(song["external_urls"]["spotify"])
        i_url.append(song["album"]["images"][1]["url"])
        
    return song_names, e_url, i_url

# Search the related artists
def search_artists_by_artist(token, artist_id):
    
    # get the json result of the target artist
    artists = get_artists_by_artist(token, artist_id)
    
    # three return elements
    artist_names = []
    e_url = []
    i_url = []
    
    #extract information from the json result
    for idx,artist in enumerate(artists):
        artist_names.append(artist['name'])
        e_url.append(artist["external_urls"]["spotify"])
        i_url.append(artist["images"][1]["url"])
        
    return artist_names, e_url, i_url

# Search the albums by artist
def search_albums_by_artist(token, artist_id):
    albums = get_albums_by_artist(token, artist_id)
    
    album_names = []
    e_url = []
    i_url = []
    
    for idx, album in enumerate(albums):
        album_names.append(album['name'])
        e_url.append(album["external_urls"]["spotify"])
        i_url.append(album["images"][1]["url"])
        
    return album_names, e_url, i_url

# Search the album by song
def search_albums_by_song(token, song_id):
    album = get_track_features(token, song_id)["album"]
    return album['name'], album["external_urls"]["spotify"], album["images"][1]["url"]

# Search the artists by song
def search_artists_by_song(token, song_id):
    # we want artists image, so we need to search each artists individually 
    
    #store all artists infor, a list of dictionary
    artists_info = get_track_features(token, song_id)["artists"]
    
    #store the name of all artists of the song
    artists_name = []
    
    #extract the content
    for artist_name in artists_info:
        artists_name.append(artist_name["name"])
        
    #search each singer by name
    artists = []
    for name in artists_name:
        artists.append( search_for_artist(token, name))
    
     # three return elements
    artist_names = []
    e_url = []
    i_url = []
    
    #extract information from the json result
    for artist in artists:
        artist_names.append(artist['name'])
        e_url.append(artist["external_urls"]["spotify"])
        i_url.append(artist["images"][1]["url"])
        
    return artist_names, e_url, i_url
    

    

# Search songs by album name
def search_songs_by_album(token, album_id):
    songs = get_songs_by_album(token, album_id)["items"]
    song_names = []
    e_url = []
    
    
    for idx, song in enumerate(songs):
        song_names.append(song['name'])
        e_url.append(song["external_urls"]["spotify"])
        
        
    return song_names, e_url

# Search songs by playlist name
def search_songs_by_playlist(token, playlist_id):
    songs = get_playlist_features(token, playlist_id)
    
    song_names = []
    e_url = []
    i_url = []
    
    for idx, song in enumerate(songs):
        if idx == 10:
            break
        song_names.append(song["track"]["name"])
        e_url.append(song["track"]["external_urls"]["spotify"])
        i_url.append(song["track"]["album"]["images"][1]["url"])
        
    return song_names, e_url, i_url

# Search the newly release album
def search_new_release_album(token):
    albums = get_for_new_release_album(token)["items"]
    album_names = []
    e_url = []
    i_url = []
    
    for idx, album in enumerate(albums):
        album_names.append(album['name'])
        e_url.append(album["external_urls"]["spotify"])
        i_url.append(album["images"][1]["url"])
        
    return album_names, e_url, i_url

# Search the artist by album
def search_artists_by_album(token, album):
    artists_info = search_for_album(token, album)['artists']
    
    #store the name of all artists of the song
    artists_name = []
        
    #extract the content
    for artist_name in artists_info:
        artists_name.append(artist_name["name"])
        
    #search each singer by name
    artists = []
    for name in artists_name:
        artists.append( search_for_artist(token, name))
    
    album_singers = []
    e_url = []
    i_url = []
    
    for idx, artist in enumerate(artists):
        album_singers.append(artist['name'])
        e_url.append(artist["external_urls"]["spotify"])
        i_url.append(artist["images"][1]["url"])
        
    return album_singers, e_url, i_url

# Return the release date of album
def release_date_by_album(token, album):
    album_release_date = search_for_album(token, album)['release_date']
    return album_release_date

# Search the recommendation base on the artist, generes, song
def get_recommendation(token, artist_id, genres_name, song_id):
    songs = recommendation(token, artist_id, genres_name, song_id)
    song_names = []
    e_url = []
    i_url = []
    
    for idx, song in enumerate(songs):
        song_names.append(song['name'])
        e_url.append(song["external_urls"]["spotify"])
        i_url.append(song["album"]["images"][1]["url"])
        
    return song_names, e_url, i_url

# Search the related artist by artist
def get_related_artist(token, artist_id):
    artists = related_artist(token, artist_id)
    artist_names = []
    e_url = []
    i_url = []
    
    for idx, artist in enumerate(artists):
        artist_names.append(artist['name'])
        e_url.append(artist["external_urls"]["spotify"])
        i_url.append(artist["images"][1]["url"])
        
    return artist_names, e_url, i_url
        
    

# Search the related artist genres by artist
def get_related_artist_genres(token, artist_id):
    genres = related_artist(token, artist_id)
    genres_names = []
    for genre in genres:
        genres_names.append(genre["genres"])
    return genres_names







##################      Main       ##################
token = get_token()
artist = "Yonezu Kenshi"
song = "晴天"
album = "24K Magic"

# Enter the artist
result = search_artists_by_album(token, album)


print(result)


# album_names = search_albums_by_artist(token, artist_id)
# for element in album_names:
#     print(element)


# search_songs_by_artist(token, artist_id)
# search_artists_by_artist(token, artist_id)

# Enter the song
# song_id = search_for_song(token, song)["id"]
# search_artists_by_song(token, song_id)
# print(search_albums_by_song(token, song_id))

# Enter the album
# album_id = search_for_album(token, album)["id"]
# print(search_artists_by_album(token, album))
# print(release_date_by_album(token, album))
# song_names = search_songs_by_album(token, album_id)
# for element in song_names:
#     print(element)

# Enter the playlist
# playlist_id = search_for_playlist(token, "death stranding")["id"]
# song_names = search_songs_by_playlist(token, playlist_id)
# for element in song_names:
#     print(element)

# Recommandation
# genres_name = "None"
# artist_id = "None"
# song_id = "None"
# print(get_recommendation(token, artist_id, genres_name, song_id))
# print(get_related_artist(token, artist_id))
# print(get_related_artist_genres(token, artist_id))
# print(search_new_release_album(token))
