#Imports
import cv2 # Computer Vision Library
import matplotlib.pyplot as plt # Library used for various visualization purposes
import numpy as np # library for doing basic matrix functions
import PIL

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.shape=shape
        self.crop_type=crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        width, height = image.size
        new_height=self.shape[0]
        new_width=self.shape[1]
        if self.crop_type=='center':
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2
        
        else:
            left=random.randint(0,width - new_width)
            right=left+new_width
            top=random.randint(0,height - new_height)
            bottom=top+new_height

        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image


        

 