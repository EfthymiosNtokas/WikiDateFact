import requests
import random
import html2text
from bs4 import BeautifulSoup
import re

# WikiSearcher: Gets a searchterm, returns pageids that match this term through wiki media api


class WikiSearcher:
    def __init__(self, searchterm, limit=20):
        self.PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": searchterm,
            "srlimit": limit
        }
        self.URL = "https://en.wikipedia.org/w/api.php"
        self.session = requests.Session()

    def get_pages(self, num=1):
        try:
            response = self.session.get(url=self.URL, params=self.PARAMS)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            if 'query' in data and 'search' in data['query'] and data['query']['search']:
                return [result['pageid'] for result in data['query']['search'][:num]] #array of size num (could be less if num>limit)
            else:
                return None  # No search results
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None


wiki = WikiSearcher("Ntokas", 4)
page1 = wiki.get_pages(20)[0]


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

#class for getting html elemnts with beautiful soup from a html text
class HtmlGetter:
    def __init__ (self,content):
        self.content=content

    def random_bullet(self):
        #20 to skip some li not good
        facts=self.content.find_all("li")[20:60]
        index = random.randint(0,40)
        fact = str(facts[index])
        #remove uncessary stuff
        fact = re.sub(r'<[^>]*>|\[[^\]]+\]', '', fact)
        return fact

   

arr = [1, 2, 3, 4]
print(arr[:6])
w = WikiScraper(page1)
info = w.get_content()
obj = HtmlGetter(info)
print(obj.random_bullet())
