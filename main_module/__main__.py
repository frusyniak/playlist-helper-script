# ask for csv path first
from handle_csv import CsvHandler
from resources import ScriptRunner

print('What is the absolute path to the csv? (press enter for placeholder default)')
inp = input()

if inp == '':
    inp = '/Users/JohnDeVries/python_projects/profanity-checker-script/data.csv'



runner = ScriptRunner(inp)
runner.get_lyrics()
