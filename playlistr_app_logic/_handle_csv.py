"""
A general purpose script for pulling all rows, but only certain columns
out of a csv.

You should turn this into a module some day.
"""

import csv
import logging

logging.basicConfig(
    filename='./log_csv_handler.log',
    filemode='w',
    level='INFO'
)

class CsvHandler():

    """
    Search a csv file for song titles and artists, and return a
    CsvHandler object with the following attributes:

    self.csv_array --> representation of original CSV in an array.
    self.user_data --> list of tuples: (song_title, band/artist_name)
    """












    # change this
    # def __init__(self, ***csv_path***):

    # to this
    def __init__(self, csv_string):

    # csv will probably be read in and passed back as a string from the
    # front end, since it'll presumably come from the google drive api
    # if this function is used at all




















        """
        Technically, csv_upload is a path string right now, which will
        probably have to be adjusted in the future.

        This is inefficient af, but who cares this is python. Also, I
        don't know why I'd ever want access to anything other than the
        list of tuples. Everything else is probably a waste, and it would
        be better if the init function could take optional kwargs of
        the columns to select. Mayabe even add functionality to select
        columns in the command line (or anyplace else) like I was thinking
        originally.
        """

        with open(csv_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            iter_indicies = {}
            for header_row in reader:
                for header in header_row:
                    if header == 'song_title':
                        iter_indicies['song_title'] = header_row.index(header)
                    elif header == 'artist_or_band':
                        iter_indicies['artist_or_band'] = header_row.index(header)

                    else:
                        pass
                break

            # make self.csv_array
            csv_array = []
            for row in reader:
                csv_array.append(row)

            # make self.data_dict. Probably won't use
            output = {}
            for attr in iter_indicies.keys():
                output.setdefault(attr, [])
            for row in csv_array:
                for attr, index in iter_indicies.items():
                    if row[index] == '':
                        continue
                    output[attr].append(row[index])


            # make self.tuples
                # note: use a list of tuples, not a nested tuple
                # so that self.tuples is mutable, and .pop() is available.
            tuples = []
            iterable = zip(output['song_title'], output['artist_or_band'])
            for zipped in iterable:
                logging.debug(zipped)
                tuples.append(zipped)

        self.csv_array = csv_array
        self.output = output
        self.tuples = tuples


if __name__ == '__main__':
    # obj = CsvHandler('/Users/JohnDeVries/Desktop/names.csv')
    # print(obj.csv_array, '\n\n\n', obj.tuples, '\n\n\n', obj.output)
    print('this file cannot run independently in this context.')
