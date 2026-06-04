import os, csv
from pprint import pprint
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup, Comment

'''
This script quick-n-dirty reads URLs from the pff-src.csv file,
fetches the HTML content for each URL, 
extracts the content within the <div id="content_row_default"> tag, 
and saves it to a file in the html directory, organized in language subfolders.
'''

def parse_csv_for_urls(csv_file):
    """
    Parses pff-src.csv and extracts URLs from columns:
    Collection_URL_NL, Collection_URL_EN, Stable_URL_English, Stable_Nederlands_URL.
    Returns a list of URLs.
    """
    urls = []
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                urls.append(row['Collection_URL_NL'])
                urls.append(row['Collection_URL_EN'])
                urls.append(row['Stable_URL_English'])
                urls.append(row['Stable_Nederlands_URL'])
        return set(urls)
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
        content_div.append(Comment(f'Source URL: {url}'))
        html_content = content_div.decode_contents()
        return html_content
    else:
        print("div#content_row_default not found in the HTML")
        return None

def parse_url(url):
    """
    Parses the URL to determine the language and file name for saving.
    Returns a file_path in the format: html/<language>/<file>.html
    """
    url_path_list = urlsplit(url).path.split("/") 
    file_name = url_path_list[-2] 
    # NL or EN
    if 'bestandsformaten' in url_path_list:
        lang = 'nl'
    else:
        lang = 'en'
    file_path = f"html/{lang}/{file_name}.html" 
    return file_path


def save_html_to_file(html_content, url):
    """
    Saves the given HTML content to a file in /html/<language>/<file>.html.
    """
    file_path = parse_url(url)
    dir_path = os.path.dirname(file_path)
    try:
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML content saved to {file_path}")
    except Exception as err:
        print(f"Error saving HTML to file: {err}")

urls_list = parse_csv_for_urls("pff-src.csv")
# print(sorted(urls_list))
url_filepath = {}
for url in urls_list:
    if url:
        # print(f"Processing URL: {url}")
        url_filepath[url] = parse_url(url)
        html = get_html(url=url)
        if html:
             save_html_to_file(html_content=html, url=url)
