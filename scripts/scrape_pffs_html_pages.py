
import os, csv
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup

'''
This script reads URLs from the Hierarchy-Preferred-Formats.csv file,
fetches the HTML content of each URL, extracts the content within the <div id="content_row_default"> tag, and saves it to a file in the
html directory, organized in language subfolders.
'''

def parse_csv_for_urls(csv_file):
    """
    Parses Hierarchy-Preferred-Formats.csv and extracts URLs from columns:
    Collection_URL_NL, Collection_URL_EN, Stable URL English, Stable Nederlands URL.
    Returns a list of URLs.
    """
    urls = []
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                urls.append(row['Collection_URL_NL'])
                urls.append(row['Collection_URL_EN'])
                urls.append(row['Stable URL English'])
                urls.append(row['Stable Nederlands URL'])
        return urls
    except Exception as err:
        print(f"Error reading CSV file: {err}")
        return []

def get_html(url):
    """
    Downloads the HTML content of the given URL and returns the content
    within the <div id="content_row_default"> tag.
    Returns None if the div is not found or the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as err:
        print(f"Error fetching URL: {err}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    content_div = soup.find("div", id="content_row_default")
    if content_div:
        return content_div.decode_contents()
    else:
        print("div#content_row_default not found in the HTML")
        return None
    
def save_html_to_file(html_content, url):
    """
    Saves the given HTML content to a file in /html/<language>/<file>.html.
    """
    url_path = urlsplit(url).path.split("/") 
    dir_path = f"html/{url_path[1].replace('bestandsformaten', 'nl')}" 
    file_path = f"{dir_path}/{url_path[3]}.html"
    try:
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML content saved to {file_path}")
    except Exception as err:
        print(f"Error saving HTML to file: {err}")

urls_list = parse_csv_for_urls("Hierarchy-Preferred-Formats.csv")
for url in urls_list:
    print(f"Processing URL: {url}")
    html = get_html(url=url)
    if html:
        save_html_to_file(html_content=html, url=url)


# TODO: 
# - fix spreadsheet URLS