from pathlib import Path
from zimscraperlib.zim.creator import Creator
import os
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

        for html_file in source_path.rglob("*.html"):
          path=str(html_file.relative_to(source_path))
          title=html_file.name
          fpath = html_file.resolve()

          if (html_file.name == "index.html"):

            creator.add_item_for(
                path=path,
                title=title,
                fpath=fpath,
                mimetype="text/html",
                is_front=True
            )
          else:
            creator.add_item_for(
                path=path,
                title=title,
                fpath=fpath,
                mimetype="text/html",
                is_front=False
            )
        # creator.add_redirect(path="", target_path="index.html", is_front=True)        
        creator.finish()

    except Exception as e:
        print(f"Error during ZIM creation: {e}")
        exit(1)