from PIL import Image
from glob import glob
import os

imagesFolder = "traditional-decor-patterns/images/"

foldersList = glob(imagesFolder+"*/")
for folder in foldersList:
	for file in glob(folder+"*.png"):
		#print(file)
		im = Image.open(file)
		rgb_im = im.convert("RGB")
		rgb_im.save(file[:-len(".png")]+".jpg", "JPEG", quality=95)
		if os.path.isfile(file):
			os.remove(file)