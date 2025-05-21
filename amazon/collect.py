from bs4 import BeautifulSoup
import os
import pandas as pd

for file in os.listdir("amazon/data"):
    with open(f"amazon/data/{file}") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc,'html.parser')
    l = soup.find("a", class_="a-link-normal s-line-clamp-2 s-link-style a-text-normal")
    
    
  



# Parse the HTML

# Find the anchor tag with the specific class
    anchor_tag = soup.find("a", class_="a-link-normal s-line-clamp-2 s-link-style a-text-normal")

# Extract the href attribute
 # Check if the element was found
    href = anchor_tag.get("href")  

    # Assuming `href` is already extracted and is a string
    Product_url = f"https://amazon.in/{href}"  # Correct string formatting
    print(Product_url)
    
    
    