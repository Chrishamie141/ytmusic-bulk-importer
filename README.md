# ytmusic-bulk-importer
Python script to bulk import songs into YouTube Music playlists
# 🎵 YouTube Music Bulk Playlist Importer

A Python automation tool that bulk imports songs into YouTube Music playlists.  
This project saves time by letting you add 100+ songs from a text file directly into a playlist, instead of adding them one by one manually.

---

## ✨ Features
- ✅ Bulk import songs from a `.txt` file  
- ✅ Create new playlists or append to existing ones  
- ✅ Search fallback (tries both songs and videos for best match)  
- ✅ Error handling & configurable delay between requests  
- ✅ Real-world automation: integrates with YouTube Music using [ytmusicapi](https://ytmusicapi.readthedocs.io/)

---

## 📂 Files
- `ytm_bulk_import.py` → The main Python script  
- `songs.txt` → Example list of songs to import  

---

## ⚙️ Requirements
- Python 3.8+  
- [ytmusicapi](https://ytmusicapi.readthedocs.io/)  

Install with:
```bash
pip install ytmusicapi
