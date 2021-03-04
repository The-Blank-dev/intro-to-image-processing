# Imports
from PIL import Image, ImageDraw
import numpy as np


def plot_boxes(image, var, output_imgs=None):  # Write the required arguments
    img = Image.fromarray((np.transpose(image, (1, 2, 0))*255).astype(np.uint8))
    #img = Image.fromarray(image*255).astype(np.uint8)
    l = len(var[1])

    for i in range(l):
        if (i >= 5):
            break
    	#assuming model gives object detection in decreasing pred score    
        label = var[1][i]
        bbox = var[0][i]
        draw = ImageDraw.Draw(img)
        draw.text([bbox[0][0], bbox[1][1]], label)
        draw.rectangle(bbox, outline='red')
        

    img.save(output_imgs)
  # The function should plot the predicted boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
