#Imports
from my_package.model import ObjectDetectionModel
from my_package.data import Dataset
from my_package.analysis.visualize import plot_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
from PIL import Image
def experiment(annotation_file, detector, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    data_set=Dataset(annotation_file,[])

    #Iterate over all data items.
    l=len(data_set)
    for i in range(len(data_set)):
        img=data_set[i]["image"]
        var=detector(img)
        plot_boxes(img,var,outputs+str(i)+".png")


    #Get the predictions from the detector.
    #done above

    #Draw the boxes on the image and save them.
    #done above

    #Do the required analysis experiments.
    an_op_filepath = "analytics_output/"

    img=data_set[9]['image']
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"original.png")

    data_set = Dataset(annotation_file,[FlipImage('horizontal')])

    img =data_set[9]['image']    
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"flip_horizontal.png")

    data_set= Dataset(annotation_file,[BlurImage(2)])

    img=data_set[9]['image']
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"blurred.png")

    data_set= Dataset(annotation_file,[RescaleImage([2*img.shape[2],2*img.shape[1]])])

    img=data_set[9]['image']
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"twicex.png")
    shape = [round(0.5*img.shape[2]),round(0.5*img.shape[1])]

    data_set= Dataset(annotation_file,[RescaleImage(shape)])

    img=data_set[9]['image']
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"halfx.png")

    data_set= Dataset(annotation_file,[RotateImage(270)])

    img=data_set[9]['image']
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"90degreeright.png")

    data_set= Dataset(annotation_file,[RotateImage(45)])

    img=data_set[9]['image']
    var=detector(img)
    plot_boxes(img,var,an_op_filepath+"45degreeleft.png")


def main():
    detector = ObjectDetectionModel()
    experiment('./data/annotations.jsonl', detector, [FlipImage(), BlurImage()],"./output_imgs/") # Sample arguments to call experiment()



if __name__ == '__main__':
    main()