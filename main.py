import cv2
from Plate_Detector import PlateDetector
from OCR import EasyOCR

def main():
    picture_number = 4

    path_to_img = f"Thai_Plate/{picture_number}.jpg"

    plateDetector = PlateDetector()
    bboxes = plateDetector.getBBox(path_to_img)
    
    reader = EasyOCR()

    img_cv = cv2.imread(path_to_img)

    for i, bbox in enumerate(bboxes):
        x1, y1, x2, y2 = bbox.numpy() # (x_min, y_min, x_max, y_max) format    

        cropped_img = img_cv[int(y1):int(y2), int(x1):int(x2)]

        preprocessed_img = plateDetector.preprocessImg(cropped_img)

        cv2.imwrite(f"Tmp{i}.jpg", preprocessed_img)

        print(reader.readText(f"Tmp{i}.jpg"))

if(__name__ == "__main__"):
    main()