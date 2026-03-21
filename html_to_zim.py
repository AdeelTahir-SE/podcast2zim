from pathlib import Path
from zimscraperlib.zim.creator import Creator
import os
import mimetypes


def site_to_zim(source_folder: str, output_file: str):

    source_path = Path(source_folder)
    output_path = Path(output_file)

    creator = Creator(
        filename=output_path,
        main_path="index.html",
        ignore_duplicates=True 
    )
    try:
        creator.config_dev_metadata(
           extra_metadata=None
        )
        creator.config_indexing(indexing=True)

        creator.start()

        for content_file in source_path.rglob("*"):
            if not content_file.is_file():
             continue

            path = str(content_file.relative_to(source_path))
            title = content_file.name
            fpath = content_file.resolve()
            guessed_mimetype = mimetypes.guess_type(str(content_file))[0] or "application/octet-stream"

            creator.add_item_for(
                path=path,
                title=title,
                fpath=fpath,
                mimetype=guessed_mimetype,
                is_front=(content_file.name == "index.html")
            )

        creator.add_redirect(path="", target_path="index.html", is_front=True)
        creator.finish()

    except Exception as e:
        print(f"Error during ZIM creation: {e}")
        exit(1)