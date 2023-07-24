import math


class Pagination:
    def __init__(self, items, pageSize = 10):
        self.items = items
        self.page_size = int(pageSize)
        self.current_page = int(1)
        self.total_pages = math.ceil(len(items) / self.page_size)

    def get_visible_items(self):
        # visible_items = []
        # for item in range(self.pageSize*(self.currentPage-1), self.pageSize*self.currentPage):
        #     visible_items.append(self.items[item])
        # self.visible_items = visible_items
        # return self.visible_items
        start = (self.current_page - 1) * self.page_size
        end = min(start + self.page_size, len(self.items))
        return self.items[start:end]

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages

    def go_to_page(self, page):
        if page > self.total_pages:
            self.current_page = self.total_pages
        elif page < 1:
            self.current_page = 1
        else:
            self.current_page = page


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())
p.previous_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())
p.go_to_page(6)
print(p.get_visible_items())
