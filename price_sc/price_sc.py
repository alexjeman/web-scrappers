import requests
from bs4 import BeautifulSoup

URL = 'https://www.ebay.com/itm/NVIDIA-GeForce-RTX-2080-TI-Founders-Edition/223866589548?epid=9026714548&hash=item341f7d116c:g:K8EAAOSw4pJeJsMs'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price_block = soup.find(id="prcIsum_bidPrice").get_text()
price = price_block[4:9]

print(price)
