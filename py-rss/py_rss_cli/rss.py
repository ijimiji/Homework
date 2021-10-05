import requests
import bs4


class ReadRSS:
    def __entry_to_text(self, entry: dict):
        title = entry["title"] if entry["title"] else "Unnamed article"
        link = entry["link"]
        description = (
            entry["description"] if entry["description"] else "No description."
        )
        pubdate = entry["pubdate"] if entry["pubdate"] else "Unknoun pubdate."
        image = entry["image"] if entry["image"] else "No image"
        return "".join(
            [
                f"Title: {title}\n"
                f"Description: {description}\n"
                f"Published: {pubdate}\n"
                f"Image: {image}\n"
                f"Read more: {link}\n"
            ]
        )

    def __create_entry(self, item):
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

    def __str__(self):
        news_count = self.settings["limit"]
        raw_news = [self.__create_entry(item) for item in self.items[0:news_count]]
        if self.settings["json"]:
            return str(raw_news)
        else:
            readable_texts = [self.__entry_to_text(entry) for entry in raw_news]
            return f"{self.channel_title}\n\n" + "\n".join(readable_texts)
