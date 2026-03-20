from zimscraperlib.zim import Creator

def site_to_zim(creator_name,site_path,zim_file_path):
  creator = Creator(
    site_path,   # site_path
    zim_file_path,      # zim_file_path
    creator_name="Podcast2Zim",  # optional metadata
    description="Offline podcast website"
  )
  creator.create_zim()
