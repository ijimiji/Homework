class Pagination:
    def __init__(self, text: str, chars_per_page: int):
        self.pages = []
        for i in range(0, len(text), chars_per_page):
            self.pages.append(text[i : i + chars_per_page])

    def page_count(self):
        return len(self.pages)

    def item_count(self):
        sum([len(page) for page in self.pages])

    def count_items_on_page(self, page_number):
        if page_number >= self.page_count():
            raise IndexError(f"Page {page_number} if out of range.")
        return len(self.pages[page_number])

    def display_page(self, page_number):
        if page_number >= self.page_count():
            raise IndexError(f"Page {page_number} if out of range.")
        return self.pages[page_number]

    def find_page(self, query):
        response = []
        for (i, page) in enumerate(self.pages):
            if query in page:
                response.append(i)
        if len(response) == 0:
            raise KeyError(f"Word {query} is not present in the pagination.")
        return response
