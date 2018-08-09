import json
from unittest import TestCase
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests


class TestFib(TestCase):
    def test_fib(self):
        assert True

    def test_scrap_some_data(self):

        # page_link = 'http://api.tvmedia.ca/tv/v4/genres/movies?api_key=881a51710c249ba3a6cf179cb54bb437'
        # page_response = json.load(urlopen(page_link))
        # page_content = soup(page_response.content, "html.parser")
        # show_data = page_content.find_all('genre')
        # print(show_data)

        genre_url = requests.get('http://api.tvmedia.ca/tv/v4/genres/movies?api_key=881a51710c249ba3a6cf179cb54bb437').text
        genre_html = soup(genre_url, "html.parser")
        print(genre_html.prettify())
        print("Hello")






