import os

from playlistr_app_logic import logic

base_dir = os.path.dirname(os.path.abspath('__file__'))

csv_path = os.path.join(base_dir, 'data.csv')
driver = logic.Driver(csv_path)
driver.command_line_sequence()
