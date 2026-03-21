# podcast2zim

Convert a podcast RSS feed into:
- a local static website (`index.html` + per-episode pages), and
- a ZIM archive (`podcast.zim`) for offline browsing.

This project parses an RSS feed, generates HTML pages, then packages those pages into a ZIM file.

## How it works

Pipeline used in `script.py`:
1. Read feed URLs from `rss_feed.py` (`feed_sources`).
2. Parse each feed with `feedparser` (`parser.py`).
3. Generate HTML with `website_generator.py`.
4. Download episode audio files into `./static_website/media/` and rewrite `<audio>` sources to local files.
5. Download episode thumbnail images into `./static_website/images/` and rewrite `<img>` sources to local files.
6. Save pages into `./static_website/`.
7. Build `podcast.zim` from all generated site files (`html_to_zim.py`).

## Requirements

- Python 3.9+
- Linux/macOS/Windows

Python packages:
- `feedparser`
- `beautifulsoup4`
- `zimscraperlib`

Install dependencies:

```bash
python3 -m pip install feedparser beautifulsoup4 zimscraperlib
```

## Usage

### 1) Set the podcast feed URL

Edit `rss_feed.py`:

```python
feed_sources = ["https://feeds.simplecast.com/54nAGcIl"]
```

You can include multiple feeds in the list.

### 2) Run the pipeline

```bash
python3 script.py
```

Optional (limit episodes):

```bash
python3 script.py 50
```

- No argument: process all available episodes.
- With a number: process only the first N episodes.

### 3) Output

After running:
- Static pages are written to `./static_website/`
  - `index.html`
  - `episode_0.html`, `episode_1.html`, ...
  - `media/episode_0.mp3`, `media/episode_1.mp3`, ...
  - `images/episode_0.jpg`, `images/episode_1.jpg`, ...
- ZIM archive is generated at:
  - `./podcast.zim`

## Project files

- `script.py` - main entry point (run this)
- `rss_feed.py` - list of RSS feed URLs
- `parser.py` - RSS parsing wrapper
- `website_generator.py` - HTML generation and file writing
- `audio_localizer.py` - download and rewrite episode audio to local files
- `thumbnail_image_localizer.py` - download and rewrite episode images to local files
- `html_to_zim.py` - convert generated HTML site to ZIM
- `test.py` - minimal local check for ZIM generation

## Notes

- The script currently executes on import because `main()` is called at the bottom of `script.py`.
- Audio and episode images are downloaded and embedded as local file paths so playback and thumbnails work offline in the generated site/ZIM.
- Episode pages are generated as HTML `<li>` snippets saved per file; they are intended to be lightweight episode views in the ZIM package.

## Troubleshooting

- `ModuleNotFoundError`: install missing package with `python3 -m pip install <package>`.
- Empty or incomplete output: verify the RSS URL is valid and reachable.
- ZIM creation issues: ensure `zimscraperlib` is installed and writable permissions exist in the project directory.