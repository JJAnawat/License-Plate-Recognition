from ultralytics import YOLO
import cv2
import numpy as np

import constants

class LetterRecognitor:
    def __init__(self):
        self.model = YOLO("../Train_Result/Letter_Recognition2/weights/best.pt")
    
    def getCenter(self, corners):
        x_coords = [corners[0], corners[2]]
        y_coords = [corners[1], corners[3]]

        center_x = np.mean(x_coords)
        center_y = np.mean(y_coords)

        return (center_x, center_y)
    
    def isSameBox(self, box1, box2, imageHeight, imageWidth): # box1 is left one while box2 is right one
        center1 = self.getCenter(box1)
        center2 = self.getCenter(box2)
        if(center1[0] > center2[0]):
            box1, box2 = box2, box1
        
        maxXLeft = box1[2]
        minXRight = box2[0]

        if(abs(center1[1] - center2[1]) > constants.YBBOX_DIS_THRESHOLD * imageHeight):
            return False
        if((minXRight - maxXLeft) > constants.XBBOX_DIS_THRESHOLD * imageWidth):
            return False
        return True
    
    def concateBoxes(self, box1, box2):
        x_coords = [box1[0][0], box1[0][2]] + [box2[0][0], box2[0][2]]
        y_coords = [box1[0][1], box1[0][3]] + [box2[0][1], box2[0][3]]

        # Find the minimum and maximum x and y coordinates
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)

        # Define the corners of the new bounding box
        new_bbox = [min_x, min_y, max_x, max_y]

        center1 = self.getCenter(box1[0])
        center2 = self.getCenter(box2[0])
        if(center1[0] > center2[0]):
            box1, box2 = box2, box1
        
        return (new_bbox, str(box1[1])+""+str(box2[1]), (box1[2]+box2[2])/2)

    def getBBox(self, path):
        results = self.model.predict(path)
        # print(results)

        results = [result.boxes for result in results]

        tmp = []
        for i in range(len(results[0].cls)):
            tmp.append((results[0].xyxy[i].numpy().tolist(), constants.LETTER_INDEX[int(results[0].cls[i].item())], results[0].conf[i].item()))

        results = tmp

        image = cv2.imread(path)
        imageHeight, imageWidth = image.shape[:2]

        ret = []
        for result in results:
            if(result[2] >= constants.OCR_CONF_THRESHOLD):
                ret.append(result)

        data_with_centers = [(item, self.getCenter(item[0])) for item in ret]
        sorted_data_with_centers = sorted(data_with_centers, key=lambda x: (x[1][0], x[1][1]))
        ret = [item[0] for item in sorted_data_with_centers]
        
        for i in range(len(ret)):
            if(ret[i] is None):
                continue
            for j in range(len(ret)):
                if(ret[j] is None):
                    continue
                if(i!=j and self.isSameBox(ret[i][0],ret[j][0],imageHeight,imageWidth)):
                    # Join box i and box j
                    newBox = self.concateBoxes(ret[i], ret[j])
                    # print(f"Join box {ret[i][0]} and box {ret[j][0]} into {newBox[0]}")
                    # Update the bounding box in the list
                    ret[j] = newBox
                    ret[i] = None
                    break
            
        ret = [box for box in ret if box is not None]

        return ret