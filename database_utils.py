import json
import os
import sys

from printing_utils import Printer

DATABASE_NAME = "database.json"

def get_database_location():
  if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
  else:
    app_path = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(app_path, DATABASE_NAME)

def load_data():
  database = get_database_location()
  Printer.print_info(database)
  with open(database, 'r') as file:
    return json.load(file)