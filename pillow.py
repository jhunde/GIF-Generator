from PIL import Image

# Create an array of images files
image_files = [
    "img/buddha-elemental-3d_1.jpg",
    "img/buddha-elemental-3d_2.jpg",
    "img/buddha-elemental-3d_3.jpg",
    "img/buddha-elemental-3d_3.jpg",
    "img/buddha-elemental-3d_2.jpg",
    "img/buddha-elemental-3d_1.jpg",
]

# Open and store all the image files
images = [Image.open(image) for image in image_files]

images[0].save(
    "output.gif", save_all=True, append_images=images[1:], duration=500, loop=0
)
