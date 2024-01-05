import time
import argparse

from concurrent.futures import ThreadPoolExecutor

from printing_utils import Printer
from database_utils import load_data
from University import University
from Crawlers import UCRCrawler, ITCRCrawler

def get_search_criteria(args):
  query="query="+ args.query if args.query else ""
  date_from_year = args.from_year
  date_to_year = args.to_year
  if query:
    query = "search?" + query
  if date_from_year:
    query += "&dateFromYear=" + date_from_year
  if date_to_year:
    query += "&dateToYear=" + date_to_year
  return query

def main():
  parser = argparse.ArgumentParser(description='Search Academic Journals')
  parser.add_argument('query', type=str, help='Search criteria without using punctuation symbols')
  parser.add_argument('--from-year', type=str, help='Start year for search', default='')
  parser.add_argument('--to-year', type=str, help='End year for search', default='')
  args = parser.parse_args()

  query = get_search_criteria(args)
  
  start_time = time.time()

  database = load_data()

  with ThreadPoolExecutor(max_workers=10) as executor:
    for university in database:
      u_url = university.get("u_url")
      u_name = university.get("u_name")
      journals = university.get("journals")
      if u_url and u_name:
        if u_name.upper() == University.UCR.name:
          futures = [executor.submit(UCRCrawler.fetch_data, u_url, journal, query) for journal in journals]
        elif u_name.upper() == University.ITCR.name:
          futures = [executor.submit(ITCRCrawler.fetch_data, u_url, journal, query) for journal in journals]

  for future in futures:
    future.result()

  end_time = time.time()
  total_time = end_time - start_time
  Printer.print_warning(f'Time: {total_time}')
  input('Press any key to exit')

if __name__ == "__main__":
  main()