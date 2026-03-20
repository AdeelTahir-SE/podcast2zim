def parsed_content_to_html(parsed_content):
    html_content=""
    for item in parsed_content:
        html_content+=f"<h2>{item.title}</h2>"
        html_content+=f"<p>{item.description}</p>"
        html_content+=f"<audio controls><source src='{item.enclosures[0].href}' type='audio/mpeg'></audio>"
    return html_content

def save_html_to_file(html):
    directory="./static_websites"
    with open("./static_websites/index.html") as f:
        f.write(html)