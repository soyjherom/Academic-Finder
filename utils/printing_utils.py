class Colors:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  WHITE = '\033[97m'
  MAGENTA = '\033[35m'

class Printer:
  
  @staticmethod
  def print_field(message):
    print(f"{Colors.MAGENTA}{message}{Colors.MAGENTA}")
  
  @staticmethod
  def print_warning(message):
    print(f"{Colors.YELLOW}{message}{Colors.YELLOW}")
  
  @staticmethod 
  def print_info(message):
    print(f"{Colors.WHITE}{message}{Colors.WHITE}")
  
  @staticmethod
  def print_finding(message):
    print(f"{Colors.GREEN}{message}{Colors.GREEN}")
  
  @staticmethod
  def print_error(message):
    print(f'{Colors.RED}Error: {message}{Colors.RED}')

  @staticmethod
  def print_error(message, url):
    print(f'{Colors.RED}Error: {message} {url}{Colors.RED}')
  
  @staticmethod
  def print_link(message):
    print(f'{Colors.BLUE}AT: {message}{Colors.BLUE}')

  @staticmethod
  def print_name_not_found():
    print(f"{Colors.RED}Name not found{Colors.RED}")

  @staticmethod
  def print_no_results(name):
    print(f"{Colors.RED}{name}: No results retrieved{Colors.RED}")