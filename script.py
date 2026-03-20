# Complete Script for podcast2zim
from rss_feed import feed_sources
from parser import feed_parser
from website_generator import parsed_content_to_html, save_html_to_file
from html_to_zim import site_to_zim
from bs4 import BeautifulSoap
def main():
    for feed_source in feed_sources:
        parsed_content=feed_parser(feed_source)
        main_page,episodes=parsed_content_to_html(parsed_content)
        save_html_to_file(main_page,"index.html")
        soup=BeautifulSoap(episodes,"html.parser")
        episodes=soup.find_all("div")
        for i,ep in enumerate(episodes):
            save_html_to_file(ep,f"episode_{i}.html")
        site_to_zim("./static_website")

main()