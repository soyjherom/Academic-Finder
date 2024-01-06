import requests

from bs4 import BeautifulSoup

from utils.printing_utils import Printer
from Result import Result

results = []

def fetch_data(u_url, journal, search_criteria, is_verbose):
  url = u_url + journal.get("id") + journal.get("url") + search_criteria
  
  if is_verbose:
    print(url)
  
  name = journal.get("name")
  
  if not name:
    Printer.print_error("No name was found, going to the next journal")
    return
  
  response = requests.post(url, data=search_criteria)
  
  if response.status_code != 200:
    Printer.print_error(response.status_code)
    return
  
  soup = BeautifulSoup(response.text, 'lxml')
  divs = soup.find_all('div', class_='obj_article_summary')
  
  if not divs:
    Printer.print_error('No results where found')
    return
  
  Printer.print_warning(f'{name}')
  Printer.print_info(f'Results: {len(divs)}')
  
  for div in divs:
    
    div_title = div.find('div',class_='title')
    
    if not div_title:
      continue
    
    title = div.get_text(strip=True)
    link = div.find('a')['href']
    result = Result(title, link)
    results.append(result)
    Printer.print_finding(title)
    Printer.print_link(link)