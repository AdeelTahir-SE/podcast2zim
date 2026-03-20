from pathlib import Path
from zimscraperlib.zim.creator import Creator

def site_to_zim(source_folder: str, output_file: str):

    source_path = Path(source_folder)
    output_path = Path(output_file)

    creator = Creator(
        filename=output_path,
        main_path=str(source_path),
        ignore_duplicates=True 
    )
    try:
        creator.config_dev_metadata()
        creator.start()

        for html_file in source_path.rglob("*.html"):
            creator.add_item_for(
                path=str(html_file.relative_to(source_path)),
                fpath=html_file,
                mimetype="text/html",
            )

        creator.finish()

    except Exception as e:
        print(f"❌ Error during ZIM creation: {e}")
        exit(1)