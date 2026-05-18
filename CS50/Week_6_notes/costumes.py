import sys
from PIL import Image #Pillow library

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# creating a gif from 2 images, save_all = save all frames, loop = 0 means infinitely run
images[0].save(
    "costumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 0
)