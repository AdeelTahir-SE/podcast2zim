from urllib.parse import urlparse
from urllib.request import Request, urlopen
from pathlib import Path
from bs4 import BeautifulSoup


def get_image_extension(image_url: str) -> str:
	parsed_url = urlparse(image_url)
	suffix = Path(parsed_url.path).suffix.lower()
	if suffix in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
		return suffix
	return ".jpg"


def download_image(image_url: str, target_path: Path) -> bool:
	if target_path.exists() and target_path.stat().st_size > 0:
		return True

	try:
		request = Request(image_url, headers={"User-Agent": "podcast2zim/1.0"})
		with urlopen(request, timeout=60) as response, target_path.open("wb") as output_file:
			output_file.write(response.read())
		return True
	except Exception as error:
		print(f"Failed to download image {image_url}: {error}")
		return False


def localize_episode_image(episode_html: str, episode_index: int, website_dir: Path) -> str:
	soup = BeautifulSoup(episode_html, "html.parser")
	image_tag = soup.find("img")

	if not image_tag:
		return str(soup)

	image_url = image_tag.get("src", "").strip()
	if not image_url:
		return str(soup)

	images_dir = website_dir / "images"
	images_dir.mkdir(parents=True, exist_ok=True)

	extension = get_image_extension(image_url)
	local_filename = f"episode_{episode_index}{extension}"
	local_path = images_dir / local_filename

	downloaded = download_image(image_url, local_path)
	if downloaded:
		image_tag["src"] = f"./images/{local_filename}"

	return str(soup)
