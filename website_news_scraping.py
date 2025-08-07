import requests
from bs4 import BeautifulSoup

# Step 1: Set a Target news URL
url = "https://bbc.com/news"

# Step 2: Use HTTP GET requests from url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
html_content = response.text

# Step 3: Do HTML parsing using beautifulsoup
soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify()[:1000]) 

# Step 4: Finding all the headline tags from the url
headlines = soup.find_all("h2")

# Step 5: Save all the headlines in a text file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for headline in headlines:
        title = headline.get_text(strip=True)
        if(title) :
            print(title)
            file.write(title + "\n")

print("All the headlines are saved in headlines.txt")
