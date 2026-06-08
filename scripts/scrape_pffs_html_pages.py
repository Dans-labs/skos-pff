import argparse
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

args = argparse.ArgumentParser(description="Index and Scrape HTML content from URLs in pff-src.csv")
args.add_argument("--csv_file", type=str, default="pff-src.csv", help="Path to the CSV file containing URLs")
args.add_argument("--output_dir", type=str, default="html", help="Directory to save the HTML files")
args.add_argument("--mode", type=str, default="index", choices=["index", "save"], help="Mode of operation: 'index' to get HTML URLs,  " \
"'save' saves HTML content to files it to files")
args = args.parse_args()
print(args)

def parse_csv_for_urls(csv_file):
    """
    Parses pff-src.csv and extracts URLs from columns:
    Collection_URL_NL, Collection_URL_EN, Stable_URL_English, Stable_Nederlands_URL.
    Returns a dictionary of URLs.
    """
    urls = {
        "collection_urls_en": [],
        "collection_urls_nl": [],
        "stable_urls_en": [],
        "stable_urls_nl": []
    }
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                urls["collection_urls_nl"].append(row['Collection_URL_NL'])
                urls["collection_urls_en"].append(row['Collection_URL_EN'])
                urls["stable_urls_en"].append(row['Stable_URL_English'])
                urls["stable_urls_nl"].append(row['Stable_Nederlands_URL'])
        for key, url_list in urls.items():
            urls[key][:] = [x for x in url_list if x != ""]  # Remove empty entries 
            urls[key] = set(url_list)  # Remove duplicates
        return urls
    except Exception as err:
        print(f"Error reading CSV file: {err}")
        return None

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

def url2localpath(url, dir, subdir):
    """
    Parses the URL to determine the language and file name for saving.
    Returns a file_path in the format: <dir>/<language>/<file>.html
    """
    url_path_list = urlsplit(url).path.split("/")
    url_path_list = [x for x in url_path_list if x != ""]  # Remove empty segments

    file_name = url_path_list[-1] 
    # print(f"file_name={file_name}")
    file_path = f"{dir}/{subdir}/{file_name}.html" 
    # print(f"file_path={file_path}")
    return file_path


def save_html_to_file(html_content, file_path):
    """
    Saves the given HTML content to a file in /html/<language>/<file>.html.
    """
    dir_path = os.path.dirname(file_path)
    try:
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
    except Exception as err:
        print(f"Error saving HTML to file: {err}")

urls_list = parse_csv_for_urls(args.csv_file)
for url_category, url_list in urls_list.items():
    # print(f'url_category: {url_category}')
    # pprint(url_list)
    for url in url_list:
        print(f"url={url}, dir={args.output_dir}")
        file_path = url2localpath(url=url, dir=args.output_dir, subdir=url_category)
        if url:
            print(f"Handling URL: {url} to be SAVED to: {file_path}")
            if args.mode == "save":
                html = get_html(url=url)
                if html:
                    save_html_to_file(html_content=html, file_path=file_path)
                    print(f"SAVED: {file_path}")
