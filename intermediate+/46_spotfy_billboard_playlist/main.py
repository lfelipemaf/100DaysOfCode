from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTFY_CLIENT_ID ="262626e4e0034e8b99ec17dafe6bc7fb"
SPOTFY_CLIENT_SECRET = "1ece72f3d4884878a5b2751ecb91b877"
APP_REDIRECT_URI = "http://example.com"

travel_date = input("\nWelcome to Music Time Machine\n\n"
                    "Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"

response = requests.get(URL, verify=False)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTFY_CLIENT_ID,
                              client_secret=SPOTFY_CLIENT_SECRET,
                              redirect_uri=APP_REDIRECT_URI,
                              scope="playlist-modify-private",
                              show_dialog=True,
                              cache_path="token.txt",
                              username="lfelipemaf",))

user_id = sp.current_user()["id"]


song_uris = []
year = travel_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)