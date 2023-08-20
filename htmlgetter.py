import random
from bs4 import BeautifulSoup
import re

#class for getting html elemnts with beautiful soup from a html text
class HtmlGetter:
    def __init__ (self,content):
        self.content=content

    def random_bullet(self):
        #20 to skip some li not good
        facts=self.content.find_all("li")[10:20]
        print(len(facts))
        print("ABOVE")
        index = random.randint(0,10)
        fact = str(facts[index])
        #remove uncessary stuff
        fact = re.sub(r'<[^>]*>|\[[^\]]+\]', '', fact)
        return fact

   