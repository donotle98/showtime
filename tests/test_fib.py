from unittest import TestCase

# import urllib2

from urllib.request import urlopen
from bs4 import BeautifulSoup


class TestFib(TestCase):
    def test_fib(self):
        assert True

    def test_scrap_some_data(self):
        print("Hi!")
        quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
        page = urlopen(quote_page)

        soup = BeautifulSoup(page, 'html.parser')

        shit_bird = soup.find('h1')
        shit_bird.get_text()
        assert shit_bird.get_text() == "Terms of Service Violation"

        print(shit_bird.get_text())

        api_key = '881a51710c249ba3a6cf179cb54bb437'
        page_link = 'http://api.tvmedia.ca/tv/v4/genres/movies?api_key=881a51710c249ba3a6cf179cb54bb437'
        from pip._vendor.urllib3 import response
        page_response = response.(page_link, timeout=)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        show_data = page_content.find_all('genre')
        print(show_data)
