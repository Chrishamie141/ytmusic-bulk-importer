import argparse
from ytmusicapi import YTMusic
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--auth", default="C:/Users/chris/browser.json")
    parser.add_argument("--songs", default="C:/Users/chris/songs.txt")
    parser.add_argument("--playlist-name", required=True, help="Playlist name to create or append to")
    parser.add_argument("--sleep", type=float, default=0.25)
    parser.add_argument("--append", action="store_true", help="Append to existing playlist instead of creating new")
    args = parser.parse_args()

    ytmusic = YTMusic(args.auth)

    # Get playlist ID
    playlist_id = None
    if args.append:
        playlists = ytmusic.get_library_playlists(limit=100)
        for pl in playlists:
            if pl["title"].lower() == args.playlist_name.lower():
                playlist_id = pl["playlistId"]
                break
        if not playlist_id:
            print(f"Playlist '{args.playlist_name}' not found.")
            return
        print(f"Appending to existing playlist: {args.playlist_name}")
    else:
        playlist_id = ytmusic.create_playlist(args.playlist_name, "Bulk imported by script")
        print(f"Created playlist: {args.playlist_name}")

    # Load songs
    with open(args.songs, encoding="utf-8") as f:
        songs = [line.strip() for line in f if line.strip()]

    for song in songs:
        try:
            results = ytmusic.search(song, filter="songs")
            if not results:
                results = ytmusic.search(song, filter="videos")
            if results:
                videoId = results[0]["videoId"]
                ytmusic.add_playlist_items(playlist_id, [videoId])
                print(f"✓ Added: {song} → {results[0]['title']} by {results[0]['artists'][0]['name']}")
            else:
                print(f"✗ Not found: {song}")
        except Exception as e:
            print(f"Error adding {song}: {e}")
        time.sleep(args.sleep)

if __name__ == "__main__":
    main()
