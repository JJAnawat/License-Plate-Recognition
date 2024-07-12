import cv2
from ultralytics import YOLO

model = YOLO("Train-Result/weights/best.pt")

picture_number = 2

path_to_img = f"Thai-plate/{picture_number}.jpg"

results = model.predict(path_to_img)

for i, (result,) in enumerate(results):
    boxes = result.boxes.xyxy[0].numpy() # (x_min, y_min, x_max, y_max) format
    x1, y1, x2, y2 = boxes

    img_cv = cv2.imread(path_to_img)

    cropped_img = img_cv[int(y1):int(y2), int(x1):int(x2)]
    cv2.imwrite(f'cropped_{picture_number}_{i+1}.jpg',cropped_img)