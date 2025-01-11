# License-Plate-Recognition

### Workflow
1. Localize the plate
2. Preprocess the plate images
3. Find the plate number
4. Identify the province

### Datasets 
- [License Plate Dataset](https://www.kaggle.com/datasets/fareselmenshawii/large-license-plate-dataset)
- [Thai Letter Dataset](https://universe.roboflow.com/magarthai/iotproject-license-plate/dataset/3/images)
- [Thai Province Dataset (containing 77 classes)](https://universe.roboflow.com/unit/license-plate-province)

### Room for improvement
- Increase the number of epochs during the training phase (currently, I've only used 1 hour of training, which may cause the model to underfit)
- Experiment with different models like ResNet50 for classifying provinces instead of using YOLO only, as the program currently does
- Explore other preprocessing techniques, as the current method seems to be reducing too much information from the images

### Main Problem
Currently, the plate localizer includes the outer boundary of the plate, which introduces noise to the OCR process. This issue can be resolved by updating the license plate dataset or manually labeling the data.