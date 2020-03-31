class Secrets:
    """
    Api keys and all that jazz.
    """
    def __init__(self):

        # this api is shit
        # mourits_lyrics_headers = {
        #     'x-rapidapi-host': "mourits-lyrics.p.rapidapi.com",
        #     'x-rapidapi-key': "bc3971f9c9msh5bacdeeea76c955p1ea8acjsnbc1102de4183"
        #     }

        # self.get_lyrics_url = 'https://mourits-lyrics.p.rapidapi.com/'
        # self.mourits_lyrics_headers = mourits_lyrics_headers


        """
        For the Musicxmatch api, the key is always passed as a parameter.
        """
        self.search = 'https://api.musixmatch.com/ws/1.1/track.search'
        self.get_song = 'https://api.musixmatch.com/ws/1.1/track.get'
        self.get_lyrics = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get'
        self.lyric_key = '5d0d8bdebb20aa7b0b99cfb0364567a3'
