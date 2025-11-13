import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE =  '@MrBeast'


def get_playlist_id():
    try: 
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json() 

        # print(json.dumps(data, indent=4))
        # print(data.items)

        channel_item = data["items"][0]
        # print(channel_item)

        channel_playlistid = channel_item["contentDetails"]["relatedPlaylists"]["uploads"] 
        print(channel_playlistid)
        # return channel_playlistid
    
    except requests.exceptions.RequestException as e:
        return e 
        # print(f"An error occurred while fetching the playlist ID: {e}")
        # return None
    
if __name__ == "__main__":
    get_playlist_id() 
    