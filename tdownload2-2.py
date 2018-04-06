import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://thumb.photo.naver.net/data16/2006/8/5/175/happyhope_175.jpg"
htmlURL = "http://google.com"

savepath1 = "D:/test1.jpg"
savepath2 = "D:/index.html"

dw.urlretrieve(imgUrl, savepath1)
dw.urlretrieve(htmlURL, savepath2)

print("다운로드 완료")
