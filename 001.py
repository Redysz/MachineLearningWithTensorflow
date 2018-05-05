from shutil import copy2
import pathlib

parentFolder = "traditional-decor-patterns/"
imagesFolder = "traditional-decor-patterns/decor/"

with open(parentFolder+"decor.csv", "r") as file:
	header = True
	for line in file:
		if header:
			header = False
			continue
		lineList = line.strip().split(',')[3:]
		if lineList[2] != "product":
			continue
		fileName = lineList[-1]
		folderName = lineList[0]
		directory = parentFolder+"images/"+folderName
		pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
		copy2(imagesFolder+fileName,directory+"/")
