import requests

from bs4 import BeautifulSoup

from printing_utils import Printer
from Result import Result

def fetch_data(u_url, journal, search_criteria):
  results = []
  url = u_url + journal.get("url") + search_criteria
  name = journal.get("name")
  if name:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'lxml')
      divs = soup.find_all('div', class_='article-summary')
      if divs:
        Printer.print_warning(f'{name}')
        Printer.print_info(f'Results: {len(divs)}')
        for div in divs:
          link = div.find('h3').find('a')
          title = link.get_text(strip=True)
          result = Result(title, link['href'])
          results.append(result)
          Printer.print_finding(title)
          Printer.print_link(link['href'])
    else:
      Printer.print_error(response.status_code)