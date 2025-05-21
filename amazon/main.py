import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd
import re
query = "Charger"
base_url = (f"https://www.amazon.in/s?k={query}&crid=11895NO5J4U0U&sprefix=%2Caps%2C280&ref=nb_sb_ss_recent_2_0_recent")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    # Add more user agents as needed
]


# Load existing data if file exists


# DataFrame to store product URLs
Product_url = []

# Scrape multiple pages
for page in range(1,3):  # Adjust the range to scrape more pages
    print(f"Scraping page {page}...")
    url = f"{base_url}&page={page}"
    headers = {"User-Agent": random.choice(user_agents)}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(random.uniform(5, 10))  # Random delay to avoid detection

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find all product links
            anchors = soup.find_all("a", class_="a-link-normal s-no-outline")
            for anchor in anchors:
                href = anchor.get("href")
                if href and "/dp/" in href:
                    if href.startswith("https://"):
                       
                       full_url = href  # Already an absolute URL
                    else:
                     full_url = f"https://www.amazon.in{href}"  # Prepend base URL for relative links
                    Product_url.append(full_url) 
                        
                   
        else:
            print(f"Failed to scrape page {page}, status code: {response.status_code}")

    except Exception as e:
        print(f"Error on page {page}: {e}")
        continue
new_df = pd.DataFrame({"Product_url": Product_url})

# Assuming 'new_df' is a DataFrame containing product URLs
# Replace 'new_df' with your actual DataFrame and column names
data_frame = new_df.copy()

# User-Agent list for rotation to mimic different browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.8",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; Nexus S 4G Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/12.246",
    # Add more up to 100...
]




for index, link in enumerate(new_df["Product_url"].values):
    if link:
        
        print(f"Index: {index}")
        
        for _ in range(1):  # Repeat scraping attempt once
            headers = {
                
          "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"


            }
            
            try:
                response = requests.get(link, headers=headers)
                time.sleep(random.uniform(5, 10))
  # Delay to avoid getting blocked
                
                # Check if the response is valid
                if response.status_code == 404:
                    print(f"Error 404 for URL: {link}")
                    break

                soup = BeautifulSoup(response.content, 'html.parser')

                
                match = re.search(r'/dp/([A-Z0-9]{10})', link) 
                asin_id = match.group(1) if match else None # Extract ASIN ID from the URL
                new_price = soup.find("span", class_="a-price-whole")
                review = soup.find("span", class_="a-icon-alt")
                no_ratings = soup.find("span", {"id": "acrCustomerReviewText"})
                no_bought_last_month = soup.find("span", {"id": "social-proofing-faceout-title-tk_bought"})
                product_title_tag = soup.find("span", {"id": "productTitle"})
                mrp_tag = soup.find("span", class_="a-size-small aok-offscreen")
                # Save details to DataFrame
                if asin_id:
                    data_frame.loc[index, "asin_id"] = asin_id
                
                if no_bought_last_month:
                    bought_text = no_bought_last_month.get_text().strip()
                    data_frame.loc[index, "bought_last_month"] = bought_text
                    print(f"Bought Last Month: {bought_text}")

                if review:
                    data_frame.loc[index, "review"] = review.get_text().strip()
                    print(f"Review: {review.get_text().strip()}")

                if no_ratings:
                    data_frame.loc[index, "num_ratings"] = no_ratings.text.strip()
                    print(f"Number of Ratings: {no_ratings.text.strip()}")

                if new_price:
                    data_frame.loc[index, "price"] = new_price.text.strip()
                    print(f"Price: {new_price.text.strip()}")

                if product_title_tag:
                     
                     product_title = product_title_tag.get_text().strip()
                     data_frame.loc[index, "title"] = product_title
                     print(f"Product Title: {product_title}")

                if mrp_tag:
                    mrp = mrp_tag.get_text().replace("M.R.P.:", "").strip()
                    data_frame.loc[index, "mrp"] = mrp
                    print(f"MRP: {mrp}")
                
                data_frame.loc[index,"Category"] = query

                # Export DataFrame to Excel after processing each product
                data_frame.to_excel("new_prices.xlsx", index=False)
            
            except Exception as e:
                print(f"Error scraping URL {link}: {e}")
                continue
