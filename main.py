import cv2
from Plate_Detector import PlateDetector
import numpy as np

def main():
    picture_number = 3

    path_to_img = f"Thai_Plate/{picture_number}.jpg"

    plateDetector = PlateDetector()
    bboxes = plateDetector.getBBox(path_to_img)
    
    img_cv = cv2.imread(path_to_img)
    
    for i, (bbox,) in enumerate(bboxes):
        x1, y1, x2, y2 = bbox.xyxy[0].numpy() # (x_min, y_min, x_max, y_max) format    

        cropped_img = img_cv[int(y1):int(y2), int(x1):int(x2)]

        cv2.imwrite("Tmp.jpg",cropped_img)

        # cv2.imshow('White Area of License Plate', result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows() 

if(__name__ == "__main__"):
    main()