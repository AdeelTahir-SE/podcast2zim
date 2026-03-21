from rss_feed import feed_sources
from parser import feed_parser
from website_generator import parsed_content_to_html, save_html_to_file
from html_to_zim import site_to_zim
from bs4 import BeautifulSoup
from pathlib import Path
from audio_localizer import localize_episode_audio
from thumbnail_image_localizer import localize_episode_image
import sys

MAX_EPISODES = int(sys.argv[1]) if len(sys.argv) > 1 else None

def main():
    for feed_source in feed_sources:

        parsed_content=feed_parser(feed_source)
        main_page,episodes=parsed_content_to_html(MAX_EPISODES,parsed_content)

        save_html_to_file(main_page,"index.html")
        
        soup=BeautifulSoup(episodes,"html.parser")
        episodes=soup.find_all("li")

        selected_episodes = episodes if MAX_EPISODES is None else episodes[:MAX_EPISODES]

        for i,ep in enumerate(selected_episodes):
            localized_episode_html = localize_episode_audio(
                str(ep),
                i,
                Path("./static_website")
            )

            localized_episode_html = localize_episode_image(
                localized_episode_html,
                i,
                Path("./static_website")
            )

            save_html_to_file(localized_episode_html,f"episode_{i}.html")

        site_to_zim( Path("./static_website"), Path("./podcast.zim"))
main()