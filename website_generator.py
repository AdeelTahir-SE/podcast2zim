import os

def parsed_content_to_html(parsed_content):
    main_page = ""
    episode = ""
    episodes_pages = ""

    episodes = parsed_content.entries
    feed_title = getattr(parsed_content.feed, "title", "Podcast")

    main_page = f"""<html>
    <head>
    <title>{feed_title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; }}
        a {{ text-decoration: none; color: #2980b9; }}
        a:hover {{ text-decoration: underline; }}
    </style>
    </head>
    <body>
    <h1>{feed_title}</h1>
    <ul>
    """

    for i, ep in enumerate(episodes):
        audio_file = ep.enclosures[0].href if ep.enclosures else getattr(ep, "link", "#")
        main_page += f'<li><a href="./episode_{i}.html">{getattr(ep, "title", "Episode")}</a></li>\n'

        episode = f"""
        <li>
            <h2>{getattr(ep, 'title', 'Episode')}</h2>
            <p>{getattr(ep, 'description', '')}</p>
            <audio controls>
                <source src="{audio_file}" type="audio/mpeg">
            </audio>
        </li>
        """
        episodes_pages += episode

    main_page += "</ul>\n</body>\n</html>"
    return main_page, episodes_pages

def save_html_to_file(html, path):
    directory = "./static_website"
    # create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, path), "w", encoding="utf-8") as f:
        f.write(html)