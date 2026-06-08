
# make depencies
# apt install pandoc 

# make clean



# make (content) html2markdown 
# pandoc -f html -t markdown_strict  html/en/aiff.html 
# * links are preserved 

.PHONY: html-download
html-download:
	mkdir html
	python scripts/scrape_pffs_html_pages.py --mode save --csv_file data/pffs_urls.csv --output_dir html