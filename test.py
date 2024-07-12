from ultralytics import YOLO

model = YOLO("trainResult/weights/best.pt")

model.predict("Thai-plate/testImg.jpg",save=True)