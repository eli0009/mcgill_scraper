import requests
from bs4 import BeautifulSoup
from pathlib import Path

root = Path(__file__).parent
courses = root / "courses"
courses.mkdir(parents=True, exist_ok=True)

class Download:

    """Download a web page using different methods."""

    def __init__(self, url=None):
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
        course_numbers = self.content.find_all('span', {'class': 'course_number'})
        return [course_number.text.strip().replace(' ', '-')
                for course_number in course_numbers]
    
if __name__ == '__main__':
    url = 'https://www.mcgill.ca/mathstat/undergraduate/programs/b-sc/minor-statistics-b-sc'
    file = courses / 'test.html'
    dl = Download(url)
    dl.get_soup(filename=str(file))
    print(dl.get_courses_from_program_page())