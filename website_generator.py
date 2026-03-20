def parsed_content_to_html(parsed_content):

    main_page=""
    episode=""
    episodes_pages=""
    episodes=parsed_content.episodes
    
    main_page=f"<h1>{parsed_content.title}</h1>"
    main_page+="<ul>"
    for i,ep in episodes:
     main_page+=f"<li><a href=./episode_{i}.html></li>"
     episode= f"""
        <div>
        <h2>{ep['title']}</h2>
        <p>{ep['description']}</p>
        <audio controls>
            <source src="../{ep['audio_file']}" type="audio/mpeg">
        </audio>
        </div>
        """
     episodes_pages+=episode
    main_page+="<ul>"
    return (main_page,episodes_pages)

   

def save_html_to_file(html,path):
    directory="./static_website"
    with open(f"./static_website/{path}","w") as f:
        f.write(html)