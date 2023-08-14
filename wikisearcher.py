import requests

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
