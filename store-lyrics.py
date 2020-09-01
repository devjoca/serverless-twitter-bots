import lyricsgenius
import os

genius = lyricsgenius.Genius(os.environ['GENIUS_ACCESS_TOKEN'])

artist = genius.search_artist("Valentín y los Volcanes",
                              sort="title",
                              artist_id=484381)
artist.save_lyrics('songs.json', overwrite=True)
