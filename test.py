import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert to grayscale
image = cv2.imread('Tmp.jpg', cv2.IMREAD_GRAYSCALE)

# Binarize the image
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Compute vertical projection
vertical_projection = np.sum(binary_image, axis=0)

# Compute horizontal projection
horizontal_projection = np.sum(binary_image, axis=1)

# Calculate border positions using the projections
dv = np.diff(vertical_projection)
dh = np.diff(horizontal_projection)

# Find maximum and minimum positions in dv and dh
ma_v = np.argmax(dv)
mi_v = np.argmin(dv)
ma_h = np.argmax(dh)
mi_h = np.argmin(dh)

# Crop the image using the detected borders
# Note: Ensure that the border indices are within the image dimensions
top_border = max(0, ma_h - 1)
bottom_border = min(binary_image.shape[0], mi_h + 1)
left_border = max(0, ma_v - 1)
right_border = min(binary_image.shape[1], mi_v + 1)

cropped_image = binary_image[top_border:bottom_border, left_border:right_border]

# Display the results
plt.figure(figsize=(10, 10))

# Original image
plt.subplot(3, 1, 1)
plt.title('Binarized Image')
plt.imshow(binary_image, cmap='gray')

# Vertical projection
plt.subplot(3, 1, 2)
plt.title('Vertical Projection')
plt.plot(vertical_projection)

# Horizontal projection
plt.subplot(3, 1, 3)
plt.title('Horizontal Projection')
plt.plot(horizontal_projection)

plt.show()

# Display cropped image
plt.figure()
plt.title('Cropped Image')
plt.imshow(cropped_image, cmap='gray')
plt.show()

# Save the cropped image
cv2.imwrite('cropped_license_plate.jpg', cropped_image)

print(f'Vertical border positions: max at {ma_v}, min at {mi_v}')
print(f'Horizontal border positions: max at {ma_h}, min at {mi_h}')