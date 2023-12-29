import requests
from bs4 import BeautifulSoup

journals = [
  {
    "name": "Actualidades Investigativas En Educacion",
    "field":"Educacion",
    "url": "https://revistas.ucr.ac.cr/index.php/aie/search/"
  },
  {
    "name": "Cuadernos de Investigación y Formación en Educación Matemática",
    "field":"Educacion",
    "url": "https://revistas.ucr.ac.cr/index.php/cifem/search/" 
  },
  {
    "name": "Revista Estudios",
    "field":"Educacion",
    "url": "https://revistas.ucr.ac.cr/index.php/estudios/search/"
  },
  {
    "name": "Gestión de la Educación",
    "field":"Educacion",
    "url":"https://revistas.ucr.ac.cr/index.php/gestedu/search/"
  },
  {
    "name": "Odovtos",
    "field":"Educacion",
    "url":"https://revistas.ucr.ac.cr/index.php/Odontos/search/"
  },
  {
    "name": "Pensar en Movimiento",
    "field":"Educacion",
    "url":"https://revistas.ucr.ac.cr/index.php/pem/search/"
  },
  {
    "name":"e-Ciencias de la Información",
    "field":"Ingenieria",
    "url":"https://revistas.ucr.ac.cr/index.php/eciencias/search/"
  },
  {
    "name":"Ingeniería",
    "field":"Ingenieria",
    "url":"https://revistas.ucr.ac.cr/index.php/ingenieria/search/"
  },
  {
    "name":"Revista de ciencia y tecnología",
    "field":"Ingenieria",
    "url":"https://revistas.ucr.ac.cr/index.php/cienciaytecnologia/search/"
  },
  {
    "name":"Infraestructura Vial",
    "field":"Ingenieria",
    "url":"https://revistas.ucr.ac.cr/index.php/vial/search/"
  },
  {
    "name":"InterSedes",
    "field":"Interdisciplinar",
    "url":"https://revistas.ucr.ac.cr/index.php/intersedes/search/"
  },
  {
    "name":"Káñina",
    "field":"Artes y letras",
    "url":"https://revistas.ucr.ac.cr/index.php/kanina/search/"
  },
  {
    "name":"Biología tropical",
    "field":"Biologia",
    "url":"https://revistas.ucr.ac.cr/index.php/rbt/search/"
  },
  {
    "name":"Revista de ciencias economicas",
    "field":"Economia",
    "url":"https://revistas.ucr.ac.cr/index.php/economicas/search/"
  },
  {
    "name":"Revista de ciencias juridicas",
    "field":"Derecho",
    "url":"https://revistas.ucr.ac.cr/index.php/juridicas/search/"
  },
  {
    "name":"Revista de ciencias sociales",
    "field":"Ciencias sociales",
    "url":"https://revistas.ucr.ac.cr/index.php/sociales/search/"
  },
  {
    "name":"Filología y Linguística de la UCR",
    "field":"Ciencias sociales",
    "url":"https://revistas.ucr.ac.cr/index.php/filyling/search/"
  },
  {
    "name":"Filosofía de la UCR",
    "field":"Ciencias sociales",
    "url":"https://revistas.ucr.ac.cr/index.php/filosofia/search/"
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
  {
    "name":"",
    "field":"",
    "url":""
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
  def print_field(message):
    print(f"{Colors.MAGENTA}{message}{Colors.MAGENTA}")
  def print_warning(message):
    print(f"{Colors.YELLOW}{message}{Colors.YELLOW}")
  def print_info(message):
    print(f"{Colors.WHITE}{message}{Colors.WHITE}")
  def print_finding(message):
    print(f"{Colors.GREEN}{message}{Colors.GREEN}")
  def print_error(message):
    print(f'{Colors.RED}Request error: {message}{Colors.RED}')
  def print_link(message):
    print(f'{Colors.BLUE}AT: {message}{Colors.BLUE}')
  

def set_search_criteria():
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

search_criteria = set_search_criteria()

for journal in journals:
  url = journal.get("url")
  if url:
    url += search_criteria
    name = journal.get("name")
    MyPrinter.print_field(f'Field: {journal.get("field")}')
    MyPrinter.print_info(f'Searching into {name}')
    MyPrinter.print_info(f'Using {url} Please wait...')
    response = requests.get(url)
    
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'lxml')
      divs = soup.find_all('div', class_='article-summary-title')
      if divs:
        MyPrinter.print_warning(f'{len(divs)} Results')
        for div in divs:
          MyPrinter.print_finding(div.get_text(strip=True))
          MyPrinter.print_link(div.find('a')['href'])
      else:
        MyPrinter.print_warning(f'{len(divs)} Results')
    else:
      MyPrinter.print_error(response.status_code)