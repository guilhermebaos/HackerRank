from html.parser import HTMLParser


# Change the methods to our specific purpose
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment ')
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)


# Initialize the parser and feed it HTML
parser = MyHTMLParser()

html = ""
for i in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
