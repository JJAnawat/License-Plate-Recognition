import cv2
import numpy as np
from matplotlib import pyplot as plt
from OCR import EasyOCR
from PIL import Image, ImageDraw, ImageFont

def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Otsu's Binarization
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Gentle denoising  
    denoised = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)

    # Optional: Enhance contrast using histogram equalization
    equalized = cv2.equalizeHist(denoised)

    # # Optional: Resize the image if necessary for your OCR model
    # resized = cv2.resize(equalized, (640, 640))

    return equalized

# Example usage
image_path = 'Tmp.jpg'
image = preprocess_image(image_path)

reader = EasyOCR()

results = reader.readText(image)

img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(img_pil)

thai_font_path = 'NotoSansThaiLooped-Regular.ttf'  # Example path to a Thai font
font = ImageFont.truetype(thai_font_path, size=12)

for (bbox, text, prob) in results:
    # Unpack the bounding box
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple([int(val) for val in top_left])
    top_right = tuple([int(val) for val in top_right])
    bottom_right = tuple([int(val) for val in bottom_right])
    bottom_left = tuple([int(val) for val in bottom_left])

    # Draw the bounding box
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1)

    draw.rectangle([top_left, bottom_right], outline='green', width=2)
    draw.text((top_left[0], top_left[1] - 4), text + str(prob), font=font, fill='green')

    print(text)

image_with_text = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# Display the image with bounding boxes
plt.imshow(cv2.cvtColor(image_with_text, cv2.COLOR_BGR2RGB))
plt.title('Image with Bounding Boxes')
plt.show()

# Save the image with bounding boxes if needed
# cv2.imwrite('output_image.jpg', image)