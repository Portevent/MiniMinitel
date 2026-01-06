from minitel.minitel_image import MinitelImage

with MinitelImage() as minitel:
    minitel._mixte_to_videotex()
    minitel.showImageBuggy("asset/logo recreated.png", "center")