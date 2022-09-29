import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re

root = Path(__file__).parent
courses = root / "courses"
courses.mkdir(parents=True, exist_ok=True)

class Download:

    """Download a web page using different methods."""

    def __init__(self, url):
        self.url = url

    def request(self, method='GET'):
        """
        return true if the request was successful, false otherwise.
        save content as BeautifulSoup object if successful.
        method can be either GET, POST, OPTIONS, HEAD, PUT, DELETE or PATCH.
        """

        result = requests.request(method, self.url)
        if result.status_code == 200:
            self.get_soup(result.content)
            return True
        else:
            return False

    def get_soup(self, content=None, filename=None):
        """get a BeautifulSoup object from the given content, or filename if
        the latter is specified.
        """
        if content is not None:
            self.content = BeautifulSoup(content, 'html.parser')
        elif filename is not None:
            with open(filename, 'r') as fp:
                file = fp.read()
                self.content = BeautifulSoup(file, 'html.parser')

    def save_soup(self, filename):
        """Save soup as a HTML document inside the course directory."""
        with open(str(courses / filename), 'w') as fp:
            print(self.content.prettify(), file=fp)

    def get_courses_from_program_page(self):
        """
        Get all courses code from soup. Course code should look like this:
        MATH 222
        COMP 551
        ECSE 539
        """
        if '/mathstat/undergraduate/programs' in self.url:
            course_numbers = self.content.find_all('span', {'class': 'course_number'})
            return [course_number.text.strip().replace(' ', '-')
                    for course_number in course_numbers]
        elif '/science/undergraduate/programs' in self.url:
            course_numbers = self.content.find_all('a',
                                                   {'class': 'program-course-title'})
            
            codes = []
            p = re.compile(r'[A-Z]{4} [0-9]{3}')
            for course_number in course_numbers:
                m = p.search(course_number.text)
                if m.group():
                    codes.append(m.group().replace(' ', '-'))
            return codes

if __name__ == '__main__':
    
    url_math = 'https://www.mcgill.ca/mathstat/undergraduate/programs/b-sc/minor-statistics-b-sc'
    url_science = 'https://www.mcgill.ca/study/2022-2023/faculties/science/undergraduate/programs/bachelor-science-bsc-major-software-engineering'
    file = courses / 'test.html'
    dl = Download(url_math)
    dl.get_soup(filename=str(file))
    print(dl.get_courses_from_program_page())
