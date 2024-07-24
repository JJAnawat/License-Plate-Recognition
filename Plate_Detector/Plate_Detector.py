from ultralytics import YOLO
import cv2

class PlateDetector:
    def __init__(self):
        self.model = YOLO("../Train_Result/Plate_Detector/weights/best.pt")
    
    def getBBox(self, path):
        results = self.model.predict(path)

        results = [result.boxes for result in results]

        self.bboxes = [box.numpy() for box in results[0].xyxy]

        return self.bboxes

    def preprocessImg(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # blur = cv2.GaussianBlur(gray,(5,5),0)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        denoised = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)
        equalized = cv2.equalizeHist(denoised)

        return equalized