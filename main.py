import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    books = []
    for i in range(1, 16):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        ol = soup.find('ol')
        articles = ol.find_all('article', class_='product_pod')
        
        for article in articles:
            image = article.find('img')
            title = image.attrs['alt']
            star = article.find('p')
            star = star['class'][1]
            price = article.find('p', class_='price_color').text
            price = float(price[2:])
            books.append([title, price, star])
    
    df = pd.DataFrame(books, columns=["Title", "Price", "Star Rating"])
    df.to_csv('books.csv')

if __name__ == "__main__":
    main()