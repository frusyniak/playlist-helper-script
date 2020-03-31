class LyricObject:
    def __init__(self, api_info, lyric_dict, student_entries):
        self.song = api_info['track_name']
        self.artist = api_info['artist_name']
        self.student_song_entry = student_entries[0]
        self.student_artist_entry = student_entries[1]

        self.lyrics = lyric_dict['lyrics_body']
