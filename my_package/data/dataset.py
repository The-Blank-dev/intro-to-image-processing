#Imports

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
#import pickle 
from PIL import Image 
import numpy as np
from transforms import FlipImage,RescaleImage,BlurImage,CropImage,RotateImage


class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file= annotation_file
        self.transforms=transforms

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        file=open(self.annotation_file,'r')
        # dictionary_list = pickle.load(file)
        l=0
        for line in file:
            l+=1
        return l

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictonary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        '''
        file=open(self.annotation_file,'r')
        # dictionary_list = pickle.load(file)
        l=0
        for x in file:
            if l== idx:
                data_point = x
                break
            l+=1
        dictionary=eval(data_point)
        img = Image.open('data/'+dictionary["img_fn"])
        if self.transforms!=None:
            for transform in self.transforms:
                img=transform(img)
         
        numpydata = np.asarray(img) 
        numpydata=numpydata.astype('float32')
        numpydata=numpydata/255.0
        numpydata_copy=numpydata
        numpydata=np.transpose(numpydata_copy,[2,0,1])
        
        new_dict={"image":numpydata,"gt_boxes":dictionary["bboxes"]}

        #print(new_dict)
        """
        for transform in self.transforms:
            new_dict["image"]=tansform(new_dict["image"])
        """
        return new_dict
        