from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

#print(soup.prettify())

top10 = soup.find_all("a", tabindex="-1")

print(top10)

for i, e in enumerate(top10,1):
    print(i, e.string)
