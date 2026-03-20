from pathlib import Path
from html_to_zim import site_to_zim

# Create a minimal HTML folder for testing
test_folder = Path("./test_site")
test_folder.mkdir(exist_ok=True)

# Create a simple HTML file
html_file = test_folder / "index.html"
html_file.write_text("<html><body><h1>Hello ZIM!</h1></body></html>", encoding="utf-8")

# Output ZIM file
output_zim = Path("./test_podcast.zim")

# Call the function to check it
site_to_zim(str(test_folder), str(output_zim))