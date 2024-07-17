import easyocr
import constants
import numpy as np
import cv2

class EasyOCR():
    def __init__(self):
        self.reader = easyocr.Reader(["th"])
    def getCenter(self, corners):
        x_coords = [corner[0] for corner in corners]
        y_coords = [corner[1] for corner in corners]

        center_x = np.mean(x_coords)
        center_y = np.mean(y_coords)

        return (center_x, center_y)
    def isSameBox(self, box1, box2, imageHeight, imageWidth): # box1 is left one while box2 is right one
        print(box1)
        center1 = self.getCenter(box1)
        center2 = self.getCenter(box2)
        if(center1[0] > center2[0]):
            box1, box2 = box2, box1
        
        maxXLeft = max(box1[1][0],box1[2][0])
        minXRight = min(box2[0][0],box2[3][0])

        if(abs(center1[1] - center2[1]) > constants.YBBOX_DIS_THRESHOLD * imageHeight):
            return False
        if((minXRight - maxXLeft) > constants.XBBOX_DIS_THRESHOLD * imageWidth):
            return False
        return True

    def readText(self, path):
        results = self.reader.readtext(path)

        image = cv2.imread(path)
        imageHeight, imageWidth = image.shape[:2]

        print(f"Height : {imageHeight}, Width : {imageWidth}")

        ret = []
        for result in results:
            if(result[2] >= constants.OCR_CONF_THRESHOLD):
                ret.append(result)
        
        for i in range(len(ret)):
            for j in range(i):
                if(self.isSameBox(ret[i][0],ret[j][0],imageHeight,imageWidth)):
                    # Join box i and box j
                    print(f"Join box {ret[i][0]} and box {ret[j][0]}")
                    pass

        return ret