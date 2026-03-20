import os

def parsed_content_to_html(parsed_content):
    main_page=""
    episode=""
    episodes_pages=""
    episodes=parsed_content.entries
    
    main_page = f"""<html>
<head>
    <meta charset="UTF-8">
    <title>{parsed_content.feed.title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f9f9f9; color: #333; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: #2980b9; }}
        a:hover {{ text-decoration: underline; }}
        audio {{ display: block; margin-top: 10px; }}
        div {{ background-color: #fff; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
<h1>{parsed_content.feed.title}</h1>
<ul>
"""
    for i, ep in enumerate(episodes):
        # Audio file
        if ep.enclosures:
            audio_file = ep.enclosures[0].href
        else:
            audio_file = ep.link  

        main_page += f'<li><a href="./episode_{i}.html">{ep.title}</a></li>\n'
        episode = f"""
        <div>
            <h2>{ep.title}</h2>
            <p>{getattr(ep, 'description', '')}</p>
            <audio controls>
                <source src="{audio_file}" type="audio/mpeg">
            </audio>
        </div>
        """
        episodes_pages += episode
    main_page += "</ul>\n</body>\n</html>"
    return (main_page, episodes_pages)


def save_html_to_file(html, path):
    directory = "./static_website"
    # create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, path), "w", encoding="utf-8") as f:
        f.write(html)