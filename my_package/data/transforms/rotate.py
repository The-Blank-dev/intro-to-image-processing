#Imports
import cv2 # Computer Vision Library
import matplotlib.pyplot as plt # Library used for various visualization purposes
import numpy as np # library for doing basic matrix functions
import PIL

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        
        # Write your code here
        self.degree=degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        rotated_image=sample.rotate(self.degree)
        return rotated_image