from cli.cache import cache_rss
import requests
import bs4
import json


class RSSReader:
    def validate_news(self, entry: dict):
        return {
            "title": entry["title"] if entry["title"] else "Unnamed article",
            "link": entry["link"],
            "description": entry["description"]
            if entry["description"]
            else "No description.",
            "pubdate": entry["pubdate"] if entry["pubdate"] else "Unknoun pubdate.",
            "image": entry["image"] if entry["image"] else "No image",
            "channel_title": self.channel_title,
        }

    def entry_to_text(self, entry: dict):
        return "".join(
            [
                f"Title: {entry['title']}\n"
                f"Description: {entry['description']}\n"
                f"Published: {entry['pubdate']}\n"
                f"Image: {entry['image']}\n"
                f"Read more: {entry['link']}\n"
            ]
        )

    def create_entry(self, item):
        return {
            "channel_title": self.channel_title,
            "title": item.find("title").text,
            "link": item.link.next_sibling.replace("\n", "")
            .replace("\t", "")
            .replace(" ", ""),
            "description": item.find("description")
            .text.replace("]]>", "")
            .replace("\n", ""),
            "pubdate": item.find("pubdate").text,
            "image": item.find("media:thumbnail")["url"],
        }

    def __init__(self, rss_url: str, settings: dict):
        self.url = rss_url
        self.settings = settings

        try:
            self.r = requests.get(rss_url)
            if self.settings["verbose"]:
                print(self.r.status_code)
        except Exception as e:
            print("Error fetching the URL: ", rss_url)
            print(e)

        try:
            self.soup = bs4.BeautifulSoup(self.r.text, "lxml")
        except Exception as e:
            print("Could not parse the xml: ", self.url)
            print(e)

        self.items = self.soup.findAll("item")
        self.channel_title = self.soup.findAll("title")[0].text

    @cache_rss
    def as_dicts(self):
        news_count = self.settings["limit"]
        raw_news = [
            self.validate_news(self.create_entry(item))
            for item in self.items[0:news_count]
        ]
        return raw_news

    def __str__(self):
        raw_news = self.as_dicts()
        if self.settings["json"]:
            return str(raw_news)
        else:
            readable_texts = [self.entry_to_text(entry) for entry in raw_news]
            return f"{self.channel_title}\n\n" + "\n".join(readable_texts)
