from PIL import Image
import os
from tqdm import tqdm


def huofilename(path):
    filenames=[]
    for filename in os.listdir(path):
        # print(filename)
        filenames.append(filename)
    return filenames



def binarize_image(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if r == 180 and g == 120 and b == 120:
                image.putpixel((x, y), (255, 255, 255))  # Set pixel to black
            else:
                image.putpixel((x, y), (0, 0, 0))  # Set pixel to white
    return image




def save_image(image, filename):
    """
    Save a PIL Image object as an image file.

    Parameters:
    image (PIL.Image.Image): The image to be saved.
    filename (str): The file name to save the image as.
    """
    image.save(filename)


#Folder where street view pictures are located after semantic segmentation.
pictureFold=r""
#Output folder
outputPath=r""
filenames=huofilename(pictureFold)
for filename in tqdm(filenames):
    image=pictureFold+'\\'+filename
    saveImage=outputPath+'\\'+filename
    image = Image.open(image)
    # img = image.convert("RGBA")
    image=binarize_image(image)
    save_image(image,saveImage)

