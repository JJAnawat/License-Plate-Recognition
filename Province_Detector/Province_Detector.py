from ultralytics import YOLO

class ProvinceDetector:
    def __init__(self):
        self.model = YOLO("../Train_Result/Province/weights/best.pt")

    def getProvince(self, path):
        results = self.model.predict(path)

        names = results[0].names

        results = [result.boxes for result in results]

        tmp = []
        for i in range(len(results[0].cls)):
            tmp.append((results[0].conf[i].item(),names[results[0].cls[i].item()]))

        sorted_tmp = sorted(tmp, reverse=True)

        # print(sorted_tmp)

        if(len(sorted_tmp) == 0):
            return None

        return sorted_tmp[0][1]