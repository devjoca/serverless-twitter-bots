import lyricsgenius

genius = lyricsgenius.Genius("GENIUS_API_KEY")

artist = genius.search_artist("Valentín y los Volcanes",
                              sort="title",
                              artist_id=484381)
artist.save_lyrics('songs.json')
