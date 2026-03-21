from pathlib import Path
from html_to_zim import site_to_zim

# Create a minimal HTML folder for testing
test_folder = Path("./static_website")
test_folder.mkdir(exist_ok=True)


# Output ZIM file
output_zim = Path("./test_podcast.zim")

print(test_folder, output_zim)
# Call the function to check it
site_to_zim(str(test_folder), str(output_zim))