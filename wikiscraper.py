import requests

from bs4 import BeautifulSoup

# wikiScraper: receives a wikipedia page_id, scrapes it and returns the content of the page in html

class WikiScraper:
    def __init__(self, page_id):
        try:
            self.page = requests.get(
                url=f"""http://en.wikipedia.org/?curid={page_id}"""
            )
            self.soup = BeautifulSoup(self.page.content, "html.parser")

            self.results = self.soup.find(id="mw-content-text")
        except:
            print("error")

    def get_content(self):
        return self.results