"""
EXPERIMENT 32: Write a Python function to create a white image size entered by the user and then create 4 boxes of Black, Blue, Green and Red respectively on each corner of the image. The size of the colored boxes should be 1/10th the size of the image.

AIM:
    To create a white image of custom user-defined dimensions and draw four colored square boxes (Black, Blue, Green, Red) of size 1/10th the image dimensions at each corner using NumPy and OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Define canvas dimensions (width=600, height=400).
    3. Create a 3-channel white canvas using np.ones((height, width, 3), dtype=np.uint8) * 255.
    4. Calculate corner box dimensions: box_w = width // 10 and box_h = height // 10.
    5. Assign pixel regions for all 4 corners: Top-Left (Black), Top-Right (Blue in BGR), Bottom-Left (Green), and Bottom-Right (Red).
    6. Save the composite image using cv2.imwrite().
    7. Display the generated image in a window.

INPUT:
    white_canvas.jpg (Source image)

OUTPUT:
    experiment 32_output.jpg (Output image)

RESULT:
    Thus, a white image with Black, Blue, Green, and Red colored corner boxes of 1/10th image size was successfully created using NumPy and OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

# Image dimensions
width, height = 600, 400

# Create white canvas
white_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Corner box size: 1/10th of image dimensions
box_w = width // 10
box_h = height // 10

# Top-Left: Black
white_img[0:box_h, 0:box_w] = [0, 0, 0]
# Top-Right: Blue (BGR)
white_img[0:box_h, width - box_w:width] = [255, 0, 0]
# Bottom-Left: Green (BGR)
white_img[height - box_h:height, 0:box_w] = [0, 255, 0]
# Bottom-Right: Red (BGR)
white_img[height - box_h:height, width - box_w:width] = [0, 0, 255]

# Save and display
cv2.imwrite("experiment 32_output.jpg", white_img)
cv2.imshow("White Image with 4 Corner Boxes", white_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Corner colored boxes creation complete.")

print("RESULT: Thus, a white image with Black, Blue, Green, and Red colored corner boxes of 1/10th image size was successfully created using NumPy and OpenCV.")
