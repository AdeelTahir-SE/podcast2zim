import os
def parsed_content_to_html(parsed_content):
    main_page=""
    episode=""
    episodes_pages=""
    episodes=parsed_content.entries
    
    main_page = f"<h1>{parsed_content.feed.title}</h1>\n<ul>\n"
    for i,ep in enumerate(episodes):
    # Audio file
     if ep.enclosures:
        audio_file = ep.enclosures[0].href
     else:
        audio_file = ep.link  
     
     main_page += f'<li><a href="./episode_{i}.html">{ep.title}</a></li>\n'
     episode= f"""
         <div>
            <h2>{ep.title}</h2>
            <p>{getattr(ep, 'description', '')}</p>
            <audio controls>
                <source src="{audio_file}" type="audio/mpeg">
            </audio>
        </div>
        """
     episodes_pages+=episode
    main_page+="<ul>"
    return (main_page,episodes_pages)

   

def save_html_to_file(html, path):
    directory = "./static_website"
    # create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, path), "w", encoding="utf-8") as f:
        f.write(html)


