from bs4 import BeautifulSoup
import lxml

html = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html, "lxml")
print(soup.h1.text)