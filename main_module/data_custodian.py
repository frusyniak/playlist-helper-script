class LyricObject:
    def __init__(self, student_entries, api_info=None, lyric_dict=None, explicit=False):
        if api_info == None:
            self.student_song_entry = student_entries[0]
            self.student_artist_entry = student_entries[1]
            return

        self.song = api_info['track_name']
        self.artist = api_info['artist_name']
        self.student_song_entry = student_entries[0]
        self.student_artist_entry = student_entries[1]

        self.lyrics = lyric_dict['lyrics_body']

        self.explicit = explicit


class CommandLineHelper:
    def __init__(self):
        pass

    def divider(self, string_):
        return string_.center((80-len(s)), '=') + '\n\n'

    def idk(self):
        for inst in lyric_objects:
            print(c('SONG'), inst.song, '\n', inst.student_song_entry)
            input()
            print(c('ARTIST'), inst.artist, '\n', inst.student_artist_entry)
            input()
            print(c('LYRICS'), inst.lyrics)
            input()
