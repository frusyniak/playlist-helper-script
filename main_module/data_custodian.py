from pyinputplus import inputMenu


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


class CommandLineHelper:
    def __init__(self):
        self.out_str = ''

    def approve_or_deny(self, linstances):
        tups = []
        for inst in linstances:
            print(self.divider('SONG'), inst.song, '\n', inst.student_song_entry)
            input()
            print(self.divider('ARTIST'), inst.artist, '\n', inst.student_artist_entry)
            input()
            print(self.divider('LYRICS'), inst.lyrics)
            input()
            print('\n\n\n****Would you like to approve or deny?****'.center(50))
            apdny = inputMenu(['x', ''])
            if apdny == 'x':
                delete_it = True
            elif apdny == '':
                delete_it = False
            else:
                raise Exception('Input error')

            tups.append((inst, delete_it))

        return tups

    def regular_lyrics(self, linstances):
        self.out_str += 'Regular_lyrics, \n'
        print(self.message('regular lyrics'))
        input()
        tups = self.approve_or_deny(linstances)
        for inst, delete_it in tups:
            if delete_it == True:
                continue
            if delete_it == False:
                self.out_str += f'{inst.song},{inst.artist}\n'

    def explicit_lyrics(self, linstances):
        self.out_str += 'Explicit, \n'
        print(self.message('explicit lyrics'))
        input()
        tups = self.approve_or_deny(linstances)
        for inst, delete_it in tups:
            if delete_it == True:
                continue
            if delete_it == False:
                self.out_str += f'{inst.song},{inst.artist}\n'

    def missing_lyrics(self, linstances):
        self.out_str += 'Missing, \n'
        print(self.message('missing lyrics'))
        input()
        tups = self.approve_or_deny(linstances)
        for inst, delete_it in tups:
            if delete_it == True:
                continue
            if delete_it == False:
                self.out_str += f'{inst.song},{inst.artist}\n'

    def write_txt_cuz_were_done(self):
        with open('output.csv' 'w') as file:
            file.write(self.out_str)

    def divider(self, string_):
        return string_.center((80-len(string_)), '=') + '\n\n'

    def message(self, category):
        rtn = f'I will show you the {category} lyrics.'
        f'{self.divider("Press enter to approve, or x to deny")}'

        return rtn
