from ultralytics import YOLO

class PlateDetector:
    def __init__(self):
        self.model = YOLO("../Train_Result/weights/best.pt")
    
    def getBBox(self, path):
        results = self.model.predict(path)

        results = [result.boxes for result in results]

        self.bboxes = results

        return results