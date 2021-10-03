import requests
import bs4


class ReadRss:
    def get_news(self, amount: int):
        pass

    def create_entry(self, item):
        return {
            "title": item.find("title").text,
            "link": item.link.next_sibling.replace("\n", "").replace("\t", ""),
            "description": item.find("description").text,
            "pubdate": item.find("pubdate").text,
        }
    def __init__(self, rss_url):
        self.url = rss_url
        try:
            self.r = requests.get(rss_url)
            self.status_code = self.r.status_code
        except Exception as e:
            print("Error fetching the URL: ", rss_url)
            print(e)
        try:
            self.soup = bs4.BeautifulSoup(self.r.text, "lxml")
        except Exception as e:
            print("Could not parse the xml: ", self.url)
            print(e)
        items = self.soup.findAll("item")
        entries = [self.create_entry(item) for item in items]
