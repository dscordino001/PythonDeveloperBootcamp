# two args -> folderName\ newFolder\
from PIL import Image
import sys
import os
# grab first and second argument

oldFolder = sys.argv[1]
newFolder = sys.argv[2]

# check if new folder exists, and if not, create it

if os.path.exists(newFolder):
    print("Folder already exists")
else:
    os.makedirs(newFolder)

# loop through New Folder and convert images

for filename in os.listdir(oldFolder):
    img = Image.open(f"{oldFolder}{filename}")
    cleanName = os.path.splitext(filename)[0]
    img.save(f"{newFolder}{cleanName}.png", "png")

