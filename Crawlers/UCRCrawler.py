import requests

from bs4 import BeautifulSoup

from printing_utils import Printer
from Result import Result

results = []

def fetch_data(u_url, journal, search_criteria):
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