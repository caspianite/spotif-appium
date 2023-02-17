import requests
from gazpacho import Soup
import pprint
# https://open.spotify.com/track/rem
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
import re

def song(link):
    page = str(requests.get(link, headers=headers).content)
    soup = Soup(page)
    song_name = soup.find("meta", {"property": "og:title"}).attrs['content'].strip("\\")
    song_duration_secs = soup.find("meta", {"name": "music:duration"}).attrs['content']
    # song_author_link = soup.find("meta", {"name": "music:musician"}).attrs['content']
    # song_author_name = Soup(str(requests.get(song_author_link, headers=headers).content)).find("meta", {"property": "og:title"}).attrs['content']
    song_album_link = soup.find("meta", {"name": "music:album"})[0].attrs["content"]
    song_album_position = soup.find("meta", {"name": "music:album:track"}).attrs["content"]
    song_release_date = soup.find("meta", {"name": "music:release_date"}).attrs['content']

    song_authors = []

    if type(soup.find("meta", {"name": "music:musician"})) == list:

        for author in soup.find("meta", {"name": "music:musician"}):
            song_authors.append({"link": author.attrs["content"], "name": Soup(str(requests.get(author.attrs["content"], headers=headers).content)).find("meta", {"property": "og:title"}).attrs['content'].strip("\\")})
    else:
        song_authors.append({"link": soup.find("meta", {"name": "music:musician"}).attrs['content'], "name": Soup(str(requests.get(soup.find("meta", {"name": "music:musician"}).attrs['content'], headers=headers).content)).find("meta", {"property": "og:title"}).attrs['content'].strip("\\")})


    information = {
        "link": link,
        "name": song_name,
        "authors": song_authors,
        "album": {
            "link": song_album_link,
            "position": song_album_position
        },
        "release_date": song_release_date,
        "duration": int(song_duration_secs)
    }
    return information


def playlist(link):
    page = str(requests.get(link, headers=headers).content)
    soup = Soup(page)
    playlist_name = soup.find("meta", {"name": "twitter:title"}).attrs['content'].strip("\\")
    playlist_duration = 0
    playlist_author = soup.find("meta", {"name": "music:creator"}).attrs['content'].split("/")[-1] # not keeping the .../user/ link breaks the project convention but there may be artists who make playlists etc.
    playlist_tracks = []

    for track in soup.find("meta", {"name": "music:song"}):
        if not track.attrs["content"].isdigit():
            track_info = song(track.attrs["content"])
            playlist_tracks.append(track_info)

            playlist_duration =+ track_info["duration"]

    information = {
        "link": link,
        "name": playlist_name,
        "author": playlist_author,
        "duration" : int(playlist_duration),
        "tracks": playlist_tracks,
        "tracks_amount": len(playlist_tracks)

    }

    return information



