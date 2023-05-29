import requests
from bs4 import BeautifulSoup
import csv
import re

# URL of the website to scrape
url = 'https://kenh14.vn/musik.chn'

# Send a GET request to the website
response = requests.get(url)

# print(response.content)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news articles on the page
news_articles = soup.find_all('h3', class_='knswli-title')

with open("test.txt", "w", encoding="utf-8") as f:
    for article in news_articles:
        f.write(str(article))

# print(news_articles)

with open("test_1.txt", "w", encoding="utf-8") as f1:
    for article in news_articles:
        anchor = soup.find('a')
        title = anchor['title']
        f1.write(str(title))
        
# # Create a CSV file to save the data
# csv_file = open('kenh14_music_news.csv', 'w', newline='', encoding='utf-8')
# writer = csv.writer(csv_file)
# writer.writerow(['Title', 'Summary', 'Link'])

# # Iterate over each news article and extract relevant information
# for article in news_articles:
#     # Extract the title
#     title = article.find('title').text.strip()
    
#     # Extract the summary
#     summary = article.find('p', class_='knswli-sapo').text.strip()
    
#     # Extract the link
#     link = article.find('a')['href']
    
#     # Write the information to the CSV file
#     writer.writerow([title, summary, link])

# # Close the CSV file
# csv_file.close()
