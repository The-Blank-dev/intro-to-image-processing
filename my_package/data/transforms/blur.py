#Imports
import cv2 # Computer Vision Library
import matplotlib.pyplot as plt # Library used for various visualization purposes
import numpy as np # library for doing basic matrix functions
from PIL import Image,ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius=5):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        self.radius=radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        blurred_im=image.filter(ImageFilter.GaussianBlur(radius = self.radius)) 
        return blurred_im

