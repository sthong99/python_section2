from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print("1", soup.select_one("li:nth-of-type(8)").string)
