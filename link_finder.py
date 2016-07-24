from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = []
        self.content = []
        self.record = False


    # When we call HTMLParser feed(), this function is called it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            test = 0
            for (attribute, value) in attrs:
                if (attribute == 'href') and ('thread' in value):
                    test = 1
                    self.url = parse.urljoin(self.base_url, value)
                    self.links.append(self.url)
                    break
            for (attribute, value) in attrs:
                if (attribute == 'onclick') and ('atarget' in value):
                    test += 1
                    if test == 2:
                        self.record = True
                        test = 0
                    break
            if test == 1:
                self.links.pop(-1)
    def handle_endtag(self, tag):
        if tag == 'a':
            self.record = False
    def handle_data(self, data):
        if self.record:
            self.content.append(data)
    def page_links(self):
        return [self.links, self.content]
