import shelve
import requests

from secrets import Secrets
from handle_csv import CsvHandler

class ScriptRunner(CsvHandler):
    def __init__(self, csv_path):

        super().__init__(csv_path)
        self.secrets = Secrets()

    def get_lyrics(self):
        """
        Get lyrics of every song in self.tuples. Create a dictionary = {
            {
                'csv_data': ('Despacito', 'Louis Fonsi'),
                'lyrics': 'lyrics go here',
            }
            {
                'csv_data': ('Alone', 'Marshmellow'),
                'lyrics': 'lyrics go here',
            }
        }
        """
        for song, artist in self.tuples:
            request_parameters = {
                'apikey': self.secrets.lyric_key,
                'q_track': song,
                'q_artist': artist,
                'f_has_lyrics': True
            }
            response = requests.get(
                self.secrets.search,
                params=request_parameters,
            )
            resp_content = response.json()  # now the response is a python dictionary
            tracks_found = resp_content['message']['body']['track_list']
            if tracks_found == []
                print('found nothing')
            breakpoint()
            print(response.text)

            input()  # don't want to make a million api requests

    def check_cache(self, track_id):


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
