import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

from Plate_Detector import PlateDetector
from OCR import EasyOCR
import constants

def readEasyOCR(path, img_height, img_width):
    reader = EasyOCR()
    ocr_results = reader.readText(path)

    plate_number = "None"
    min_dist = -1
    for ocr_result in ocr_results:
        center = reader.getCenter(ocr_result[0])
        cur_dist = abs(center[0] - img_width * constants.PLATE_NUM_XPOS) + abs(center[1] - img_height * constants.PLATE_NUM_YPOS)
        if(min_dist == -1):
            min_dist = cur_dist
            plate_number = ocr_result[1]
        if(cur_dist < min_dist):
            min_dist = cur_dist
            plate_number = ocr_result[1]

    return plate_number

def main():
    picture_number = 1

    path_to_img = f"Thai_Plate/{picture_number}.jpg"

    plateDetector = PlateDetector()
    bboxes = plateDetector.getBBox(path_to_img)

    img_cv = cv2.imread(path_to_img)

    img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)

    thai_font_path = 'Fonts/NotoSansThaiLooped-Regular.ttf'  # Example path to a Thai font
    font = ImageFont.truetype(thai_font_path, size=20)

    for i, (x1, y1, x2, y2) in enumerate(bboxes): # (x_min, y_min, x_max, y_max) format    
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        img_size = (y2-y1)*(x2-x1)
        img_height, img_width = y2-y1, x2-x1

        draw.rectangle([(x1, y1), (x2, y2)], outline='green', width=2)

        if(img_size < constants.IMG_SIZE_THRESHOLD): # Image size threshold
            draw.text((x1, y1 - 30), "Plate is too small", font=font, fill='green')
            continue

        cropped_img = img_cv[y1:y2, x1:x2]

        preprocessed_img = plateDetector.preprocessImg(cropped_img)
        cv2.imwrite(f"Cropped_{i+1}.jpg", preprocessed_img)

        plate_number_EasyOCR = readEasyOCR(f"Cropped_{i+1}.jpg", img_height, img_width)

        draw.text((x1, y1 - 30), f"EasyOCR : {plate_number_EasyOCR}", font=font, fill='green')

    image_with_text = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    cv2.imshow(f"{picture_number}.jpg",cv2.cvtColor(image_with_text, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if(__name__ == "__main__"):
    main()