#Imports
import cv2 # Computer Vision Library
import matplotlib.pyplot as plt # Library used for various visualization purposes
import numpy as np # library for doing basic matrix functions
import PIL

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.flip_type=flip_type
        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        if self.flip_type=='horizontal':
            flipped_image=image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        else:
            flipped_image=image.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        return flipped_image
       