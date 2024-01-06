import requests

from bs4 import BeautifulSoup

from utils.printing_utils import Printer
from Result import Result

def fetch_data(u_url, journal, search_criteria, is_verbose):
  results = []
  url = u_url + journal.get("id") + journal.get("url") + search_criteria
  
  if is_verbose:
    print(url)
  
  name = journal.get("name")
  if not name:
    Printer.print_error("No name specified")
    return
        
  response = requests.get(url)
  if response.status_code != 200:
    Printer.print_error(response.status_code)
    return
          
  soup = BeautifulSoup(response.text, 'lxml')
  divs = soup.find_all('div', class_='article-summary')
  if not divs:
    Print.print_error('No articles')
    return
      
  Printer.print_warning(f'{name}')
  Printer.print_info(f'Results: {len(divs)}')
  for div in divs:
    link = div.find('h3').find('a')
    title = link.get_text(strip=True)
    result = Result(title, link['href'])
    results.append(result)
    Printer.print_finding(title)
    Printer.print_link(link['href'])