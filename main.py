import cv2
from Plate_Detector import PlateDetector
from OCR import EasyOCR
import constants

def main():
    picture_number = 4

    path_to_img = f"Thai_Plate/{picture_number}.jpg"

    plateDetector = PlateDetector()
    bboxes = plateDetector.getBBox(path_to_img)
    
    reader = EasyOCR()

    img_cv = cv2.imread(path_to_img)

    for i, (x1, y1, x2, y2) in enumerate(bboxes): # (x_min, y_min, x_max, y_max) format    
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        img_size = (y2-y1)*(x2-x1)

        if(img_size < constants.IMG_SIZE_THRESHOLD): # Image size threshold
            print(f"Image {i+1} is too small")
            continue

        cropped_img = img_cv[y1:y2, x1:x2]

        preprocessed_img = plateDetector.preprocessImg(cropped_img)

        cv2.imwrite(f"Cropped_{i+1}.jpg", preprocessed_img)

        print(reader.readText(f"Cropped_{i+1}.jpg"))

if(__name__ == "__main__"):
    main()