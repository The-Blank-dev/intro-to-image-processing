#Imports
import cv2 # Computer Vision Library
import matplotlib.pyplot as plt # Library used for various visualization purposes
import numpy as np # library for doing basic matrix functions
import PIL

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.op_size=output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        width, height = image.size
        if isinstance(self.op_size, int):
            if(height>width):
                resized_im=image.resize((self.op_size , height * self.op_size /width))
            else:
                resized_im=image.resize((width * self.op_size /height,self.op_size))
        else:
            resized_im=image.resize(self.op_size)
        return resized_im
