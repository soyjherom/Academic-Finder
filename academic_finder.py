import time
import argparse

from concurrent.futures import ThreadPoolExecutor

from utils.printing_utils import Printer
from utils.database_utils import load_data
from utils.search_criteria_utils import get_search_criteria, get_form_data_criteria
from University import University
from crawlers import UCRCrawler, ITCRCrawler, UNACrawler

def main():
  parser = argparse.ArgumentParser(description='Search Academic Journals')
  parser.add_argument('query', type=str, help='Search criteria without using punctuation symbols')
  parser.add_argument('--from-year', type=str, help='Start year for search', default='')
  parser.add_argument('--to-year', type=str, help='End year for search', default='')
  parser.add_argument('--u', type=str, help='University', default='ALL')
  parser.add_argument('--id', type=str, help="Journal ID", default='')
  parser.add_argument('--v', type=bool, help="Verbose URL", default=False)

  args = parser.parse_args()

  uni = args.u
  is_verbose = args.v

  query = get_search_criteria(args) if uni and uni != University.UNA else get_form_data_criteria(args)
  
  start_time = time.time()

  database = load_data()

  journal_id = args.id

  with ThreadPoolExecutor(max_workers=10) as executor:
    for university in database:
      u_url = university.get("u_url")
      u_name = university.get("u_name")
      journals = university.get("journals")
      if journal_id:
        journals = [journal for journal in journals if journal['id']==journal_id]
      if u_url and u_name:
        if u_name.upper() == University.UCR.name and (uni == University.ALL.name or uni == University.UCR.name):
          futures = [executor.submit(UCRCrawler.fetch_data, u_url, journal, query, is_verbose) for journal in journals]
        elif u_name.upper() == University.ITCR.name and (uni==University.ALL.name or uni == University.ITCR.name):
          futures = [executor.submit(ITCRCrawler.fetch_data, u_url, journal, query, is_verbose) for journal in journals]
        elif u_name.upper() == University.UNA.name and (uni==University.ALL.name or uni == University.UNA.name):
          futures = [executor.submit(UNACrawler.fetch_data, u_url, journal, query, is_verbose) for journal in journals]

  for future in futures:
    future.result()

  end_time = time.time()
  total_time = end_time - start_time
  Printer.print_warning(f'Time: {total_time}')
  input('Press any key to exit')

if __name__ == "__main__":
  main()