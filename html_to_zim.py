from zimscraperlib.zim import Creator

def site_to_zim(site_path,zim_file_path):
  creator = Creator(
    main_path=site_path,
    filename=zim_file_path,  
  )
  creator.create_zim()
