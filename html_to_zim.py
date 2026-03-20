from zimscraperlib.zim import Creator

def site_to_zim(title,site_path,zim_file_path):
 creator=Creator(
    title=title,
    filename=zim_file_path,
    lang="en"
 )
 creator.add_directory(site_path)
 creator.create_zim()
