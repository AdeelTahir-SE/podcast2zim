from urllib.parse import urlparse
from urllib.request import Request, urlopen
from pathlib import Path
from bs4 import BeautifulSoup


def get_audio_extension(audio_url: str) -> str:
    parsed_url = urlparse(audio_url)
    suffix = Path(parsed_url.path).suffix.lower()
    if suffix in {".mp3", ".m4a", ".aac", ".ogg", ".wav", ".opus"}:
        return suffix
    return ".mp3"


def download_audio(audio_url: str, target_path: Path) -> bool:
    if target_path.exists() and target_path.stat().st_size > 0:
        return True

    try:
        request = Request(audio_url, headers={"User-Agent": "podcast2zim/1.0"})
        with urlopen(request, timeout=60) as response, target_path.open("wb") as output_file:
            output_file.write(response.read())
        return True
    except Exception as error:
        print(f"Failed to download audio {audio_url}: {error}")
        return False


def localize_episode_audio(episode_html: str, episode_index: int, website_dir: Path) -> str:
    soup = BeautifulSoup(episode_html, "html.parser")
    source_tag = soup.find("source")

    if not source_tag:
        return str(soup)

    audio_url = source_tag.get("src", "").strip()
    if not audio_url:
        return str(soup)

    media_dir = website_dir / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    extension = get_audio_extension(audio_url)
    local_filename = f"episode_{episode_index}{extension}"
    local_path = media_dir / local_filename

    downloaded = download_audio(audio_url, local_path)
    if downloaded:
        source_tag["src"] = f"./media/{local_filename}"

    return str(soup)