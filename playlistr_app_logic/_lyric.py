class LyricObject:
    def __init__(self, student_entries, api_info=None, lyric_dict=None, explicit=False):
        if api_info == None:
            self.student_song_entry = student_entries[0]
            self.student_artist_entry = student_entries[1]
            self.song = student_entries[0]
            self.artist = student_entries[1]
            return

        self.song = api_info['track_name']
        self.artist = api_info['artist_name']
        self.student_song_entry = student_entries[0]
        self.student_artist_entry = student_entries[1]

        self.lyrics = lyric_dict['lyrics_body']

        self.explicit = explicit
