from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="bd64dd7a6d764381a94e19cff86cb5d2",
        client_secret="b31c74e750c340188c79a8c3f71e7fba",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("which year do you want to travlel? Type in format YYYY-MM-DD: ")

billboard_page = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(billboard_page.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

uris = []
year = date.split("-")[0]

for song in song_names:
  result = sp.search(q=f"track:{song} year:{year}", type="track")
  try:
    uri = result["tracks"]["items"][0]["uri"]
    uris.append(uri)
  except IndexError:
    print(f"{song} doesn't exist in Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=uris)