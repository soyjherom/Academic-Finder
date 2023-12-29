import requests
import time

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

from printing_utils import Printer
from database_utils import load_data

class Result:
  def __init__(self, title, url):
    self.title = title
    self.url = url

results = []

def fetch_journal_data(u_name, u_url, journal, search_criteria):
  url = u_url + journal.get("url") + search_criteria
  name = journal.get("name")
  if name:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'lxml')
      divs = soup.find_all('div', class_='article-summary-title')
      if divs:
        Printer.print_warning(f'{name}')
        Printer.print_info(f'Results: {len(divs)}')
        for div in divs:
          title = div.get_text(strip=True)
          link = div.find('a')['href']
          result = Result(title, link)
          results.append(result)
          Printer.print_finding(title)
          Printer.print_link(link)
    else:
      Printer.print_error(response.status_code)

def get_search_criteria():
  search_criteria = input('Please enter a search criteria without using punctuation symbols: ')
  search_criteria = search_criteria.replace(' ','+') if search_criteria else ''
  query="query="+search_criteria if search_criteria else ""
  date_from_year = input("From what year? ")
  date_to_year = input("To what year? ")
  if query:
    search_criteria = "search?" + query
  if date_from_year:
    search_criteria += "&dateFromYear=" + date_from_year
  if date_to_year:
    search_criteria += "&dateToYear=" + date_to_year
  return search_criteria

def main():
  search_criteria = get_search_criteria()
  
  start_time = time.time()

  database = load_data()

  with ThreadPoolExecutor(max_workers=10) as executor:
    for university in database:
      u_url = university.get("u_url")
      u_name = university.get("u_name")
      if u_url and u_name:
        futures = [executor.submit(fetch_journal_data, u_name, u_url, journal, search_criteria) for journal in university.get("journals")]

  for future in futures:
    future.result()

  end_time = time.time()
  total_time = end_time - start_time
  Printer.print_warning(f'Time: {total_time}')
  input('Press any key to exit')

if __name__ == "__main__":
  main()