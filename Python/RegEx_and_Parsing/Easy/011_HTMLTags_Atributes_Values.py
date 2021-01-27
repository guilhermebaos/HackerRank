from html.parser import HTMLParser


# Change the methods to our specific purpose
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for param, value in attrs:
            print(f'-> {param} > {value}')

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for param, value in attrs:
            print(f'-> {param} > {value}')


# Initialize the parser and feed it HTML
parser = MyHTMLParser()

n = int(input())
html = ''
for _ in range(n):
    html += str(input()) + '\n'
parser.feed(html)
