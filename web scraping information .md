# DATA web scraping
import requests
from wsgiref import headers
query = input("enter a name thta u want to crawl")

url='https://sogou.com/web?query={query}'

dic = {
    "user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=dic)


print(resp)
print(resp.text)
