import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import csv
import this

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

def get_amazon_price(dom):

    try:
        price = dom.xpath('//span[@class="a-price-whole"]/text()')
        price_fraction = dom.xpath('//span[@class="a-price-fraction"]/text()')[0]
        return int(price), int(price_fraction)
    except Exception as e:
        return None
    
def is_available(dom):

    try:
        text = dom.xpath('//span[@class="a-size-medium a-color-success"]/text()')[0]
        if 'In Stock.' in text:
            return True
    except Exception as e:
        return False

def get_product_name(dom):
    try:
        name = dom.xpath('//span[@id="productTitle"]/text()')
        [name.strip() for name in name]
        return name[0]
    except Exception as e:
        name = 'Not Available'
        return None
    

def is_free_shipping(dom):
    try:
        text = dom.xpath('//span[@id="price-shipping-message"]/text()')
        if 'Free Shipping' in text:
            return True
    except Exception as e:
        name = 'Not Available'
        return None


if __name__ == "__main__":
    product_url = 'https://www.amazon.com/dp/B0BFKJJ59R/ref=va_live_carousel?pf_rd_r=APHYNHTW0F46Z6KEKBCT&pf_rd_p=6b7fa469-70d3-4bdd-a659-1decabecaf6b&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=HighVelocityEvent&pf_rd_i=deals_1_desktop&pf_rd_s=slot-13&linkCode=ilv&tag=onamzalicecla-20&ascsubtag=Christmas_Presents_More_221216114525&asc_contentid=amzn1.amazonlive.broadcast.7285cfd5-7658-4c61-a396-61a3c7159487&pd_rd_i=B0BFKJJ59R&th=1&psc=1'
    response = requests.get(product_url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    main_dom = et.HTML(str(soup))
    print(get_amazon_price(main_dom))