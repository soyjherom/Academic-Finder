import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class Result:
  def __init__(self, title, url):
    self.title = title
    self.url = url

results = []

database = [
  {
    "u_name": "UCR",
    "u_url": "https://revistas.ucr.ac.cr/index.php/",
    "journals":[
      {
        "name": "Actualidades Investigativas En Educacion",
        "field":"Educacion",
        "url": "aie/search/"
      },
      {
        "name": "Cuadernos de Investigación y Formación en Educación Matemática",
        "field":"Educacion",
        "url": "cifem/search/" 
      },
      {
        "name": "Revista Estudios",
        "field":"Educacion",
        "url": "estudios/search/"
      },
      {
        "name": "Gestión de la Educación",
        "field":"Educacion",
        "url":"gestedu/search/"
      },
      {
        "name": "Odovtos",
        "field":"Educacion",
        "url":"Odontos/search/"
      },
      {
        "name": "Pensar en Movimiento",
        "field":"Educacion",
        "url":"pem/search/"
      },
      {
        "name":"e-Ciencias de la Información",
        "field":"Ingenieria",
        "url":"eciencias/search/"
      },
      {
        "name":"Ingeniería",
        "field":"Ingenieria",
        "url":"ingenieria/search/"
      },
      {
        "name":"Revista de ciencia y tecnología",
        "field":"Ingenieria",
        "url":"cienciaytecnologia/search/"
      },
      {
        "name":"Infraestructura Vial",
        "field":"Ingenieria",
        "url":"vial/search/"
      },
      {
        "name":"InterSedes",
        "field":"Interdisciplinar",
        "url":"intersedes/search/"
      },
      {
        "name":"Káñina",
        "field":"Artes y letras",
        "url":"kanina/search/"
      },
      {
        "name":"Biología tropical",
        "field":"Biologia",
        "url":"rbt/search/"
      },
      {
        "name":"Revista de ciencias economicas",
        "field":"Economia",
        "url":"economicas/search/"
      },
      {
        "name":"Revista de ciencias juridicas",
        "field":"Derecho",
        "url":"juridicas/search/"
      },
      {
        "name":"Revista de ciencias sociales",
        "field":"Ciencias sociales",
        "url":"sociales/search/"
      },
      {
        "name":"Filología y Linguística de la UCR",
        "field":"Ciencias sociales",
        "url":"filyling/search/"
      },
      {
        "name":"Filosofía de la UCR",
        "field":"Ciencias sociales",
        "url":"filosofia/search/"
      },
      {
        "name":"",
        "field":"",
        "url":""
      },
      {
        "name":"",
        "field":"",
        "url":""
      },
    ] 
  },
  {
    "u_name": "",
    "u_url": "",
    "journals":[
      {
        "name":"",
        "field":"",
        "url":"",
      }
    ]
  },
]

class Colors:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  WHITE = '\033[97m'
  MAGENTA = '\033[35m'

class MyPrinter:
  def print_field(self, message):
    print(f"{Colors.MAGENTA}{message}{Colors.MAGENTA}")
  def print_warning(self, message):
    print(f"{Colors.YELLOW}{message}{Colors.YELLOW}")
  def print_info(self, message):
    print(f"{Colors.WHITE}{message}{Colors.WHITE}")
  def print_finding(self, message):
    print(f"{Colors.GREEN}{message}{Colors.GREEN}")
  def print_error(self, message):
    print(f'{Colors.RED}Error: {message}{Colors.RED}')
  def print_link(self, message):
    print(f'{Colors.BLUE}AT: {message}{Colors.BLUE}')

def fetch_journal_data(u_name, u_url, journal):
  url = u_url + journal.get("url") + search_criteria
  name = journal.get("name")
  if name:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'lxml')
      divs = soup.find_all('div', class_='article-summary-title')
      if divs:
        MyPrinter.print_warning(f'{name}')
        MyPrinter.print_info(f'Results: {len(divs)}')
        for div in divs:
          title = div.get_text(strip=True)
          link = div.find('a')['href']
          result = Result(title, link)
          results.append(result)
          MyPrinter.print_finding(title)
          MyPrinter.print_link(link)
    else:
      MyPrinter.print_error(response.status_code)

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

search_criteria = get_search_criteria()

with ThreadPoolExecutor(max_workers=10) as executor:
  for university in database:
    u_url = university.get("u_url")
    u_name = university.get("u_name")
    if u_url and u_name:
      futures = [executor.submit(fetch_journal_data, u_name, u_url, journal) for journal in university.get("journals")]

for future in futures:
  future.result()