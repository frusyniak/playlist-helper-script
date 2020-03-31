import shelve
import requests

from secrets import Secrets
from handle_csv import CsvHandler


class ScriptRunner(CsvHandler):
    def __init__(self, csv_path):

        super().__init__(csv_path)
        self.secrets = Secrets()
        self.lyrics = ScriptRunner.get_lyrics(self)

    def get_lyrics(self):
        """
        This is the master function which initiates a function chain:
            * get track id's
            * pop tracks initially identified as explicit right away
            *
            * check cache
            * pull lyrics from cache, if possible
            * otherwise get lyrics from api
            *
        """

        self.get_good_track_ids()

        """
        Now, these are defined:
            self.good_ids
            self.no_id_found
            self.explicit_tracks
        """
        lyrics = []
        for item in self.good_ids:
            t, api_info = item

            # make request
            request_parameters = {
                'apikey': self.secrets.lyric_key,
                'track_id': api_info['track_id']
            }
            response = requests.get(
                self.secrets.get_lyrics,
                params=request_parameters,
            )
            lyric_dict = response.json()['message']['body']['lyrics']
            lyrics = lyric_dict['lyrics_body']
            breakpoint()

        return None # make sure you return something back to the init

    def get_good_track_ids(self):
        """
        * In the "parse resposne section," I only take the first
            result of the api response, because responses are ranked
            by popularity, adn the first is the most popular.

        * enumerate() will return an iterator, so hopefully popping
            list items won't mess with the list during the
            iteration.

        * found_something data structure:
            [
                (
                    (song, artist),
                    (dict_from_api)
                ),
            ]

        * found_nothing and explicit_tracks are both just
            popped tuples, and the api data is abandoned behind.
        """
        DEBUG_READ_SHELF = True # skip api requests, and use shelve if the is known to have all api data
        DEBUG_WRITE_SHELF = False
        found_nothing = []
        found_something = []
        explicit_tracks = []
        for index, tuple_ in enumerate(self.tuples):
            if DEBUG_READ_SHELF:
                break
            # unpack tuple
            song, artist = tuple_

            # make request
            request_parameters = {
                'apikey': self.secrets.lyric_key,
                'q_track': song,
                'q_artist': artist,
                'f_has_lyrics': True  # filter: must have lyrics
            }
            response = requests.get(
                self.secrets.search,
                params=request_parameters,
            )
            print(f'made request {index} times')

            # parse response
            resp_content: dict = response.json()
            result_list = resp_content['message']['body']['track_list']

            # log tracks without results
            if result_list == []:
                found_nothing.append(self.tuples.pop(index))
                continue
            else:
                result = result_list[0]['track']
            # immediately pop tracks that the api says are explicit
            if result['explicit'] == 1:
                explicit_tracks.append(
                    (
                        self.tuples.pop(index),
                        result
                    )
                )
                continue

            found_something.append((tuple_, result))
            print(len(found_something))

        if DEBUG_READ_SHELF:
            with shelve.open('resources_cache', writeback=True) as db:
                found_something = db['found']
                found_nothing   = db['nothing']
                explicit_tracks = db['explicit']

        if DEBUG_WRITE_SHELF:
            with shelve.open('resources_cache', writeback=True) as db:
                db['found']     = found_something
                db['nothing']   = found_nothing
                db['explicit']  = explicit_tracks

        self.good_ids = found_something
        self.no_id_found = found_nothing
        self.explicit_tracks = explicit_tracks

        return


    def lyrics_are_cached(self, track_id):
        """
        Returns boolean indicating whether a requested track id is
        cached.
        """
        with shelve.open('resources_cache') as db:
            try:
                db[track_id]
                cached = True
            except KeyError:
                cached = False

        return cached

    def write_to_cache(self, result_list):
        """
        Adds new lyrics to the cache if they are not there already.
        """
        with shelve.open('resources_cache') as db:
            for csv_data, api_data in result_list:
                pass



if __name__ == '__main__':

    import os
    base_dir = os.path.dirname(os.path.abspath('__file__'))

    runner_instance = ScriptRunner(
            os.path.join(
                base_dir,
                'tests',
                'mocks',
                'sample_data.csv',
            )
        )
