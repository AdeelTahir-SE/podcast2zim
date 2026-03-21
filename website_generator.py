import os
from datetime import datetime

def parsed_content_to_html(MAX_EPISODES,parsed_content, podcast_image=None):

    main_page = ""
    episodes_pages = ""

    episodes = parsed_content.entries[:MAX_EPISODES] if MAX_EPISODES else parsed_content.entries
    feed_title = getattr(parsed_content.feed, "title", "Podcast")

    # Inline style for main page and body
    body_style = "font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;" \
                 "background-color:#121212;color:#f0f0f0;margin:20px;"
    h1_style = "color:#ffffff;font-size:2.5em;margin-bottom:20px;text-align:center;"
    ul_style = "list-style:none;padding:0;"

    main_page = f"""<html>
    <head><title>{feed_title}</title></head>
    <body style="{body_style}">
        <h1 style="{h1_style}">{feed_title}</h1>
        {f'<img src="{podcast_image}" style="display:block;max-width:300px;height:auto;border-radius:15px;margin:0 auto 30px auto;box-shadow:0 4px 15px rgba(0,0,0,0.7);">' if podcast_image else ''}
        <ul style="{ul_style}">
    """

    for i, ep in enumerate(episodes):
        title = getattr(ep, "title", "Episode")
        description = getattr(ep, "subtitle", getattr(ep, "description", ""))
        audio_file = ep.enclosures[0].href if ep.enclosures else getattr(ep, "link", "#")
        image = getattr(ep, "image", {}).get("href", "")
        authors = [a.get("name", "") for a in getattr(ep, "authors", [])]
        published = getattr(ep, "published", "")

        try:
            published_dt = datetime(*ep.published_parsed[:6])
            published_str = published_dt.strftime("%B %d, %Y")
        except:
            published_str = published

        # Add to main page
        main_page += f'<li><a href="./episode_{i}.html" style="color:#1e90ff;text-decoration:none;">{title}</a></li>\n'

        # Inline CSS for episode card
        li_style = "background-color:#1e1e1e;margin-bottom:20px;padding:20px;text-align:center;" \
                   "border-radius:15px;box-shadow:0 4px 12px rgba(0,0,0,0.5);"
        h2_style = "color:#ffcc00;margin-bottom:5px;"
        h3_style = "color:#bbbbbb;margin-top:5px;font-weight:normal;"
        p_style = "line-height:1.6em;margin-top:10px;color:#bbbbbb"
        img_style = "max-width:100%;height:auto;border-radius:10px;margin:15px 0;box-shadow:0 2px 8px rgba(0,0,0,0.6);"
        audio_style = "width:100%;margin-top:10px;outline:none;"

        episode_html = f"""
        <li style="{li_style}">
            <h2 style="{h2_style}">{title}</h2>
            <h3 style="{h3_style}">By: {', '.join(authors)} | Published: {published_str}</h3>
            {f'<img src="{image}" style="{img_style}">' if image else ''}
            <p style="{p_style}">{description}</p>
            <audio controls style="{audio_style}">
                <source src="{audio_file}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </li>
        """

        episodes_pages += episode_html

    main_page += "</ul>\n</body>\n</html>"

    return main_page, episodes_pages







def save_html_to_file(html, path):
    

    directory = "./static_website"
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, path), "w", encoding="utf-8") as f:
        f.write(html)