"""
EXPERIMENT 33: Write a Python function to create a white image size entered by the user and then create a shape of Rectangle using Open CV.

AIM:
    To create a white image of custom dimensions and draw a rectangle geometric shape using OpenCV cv2.rectangle function.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Define image dimensions (width=600, height=400).
    3. Create a 3-channel white canvas using np.ones() * 255.
    4. Specify diagonal rectangle vertex coordinates pt1 = (100, 80) and pt2 = (500, 320).
    5. Draw the rectangle on the canvas using cv2.rectangle() with specified color and line thickness.
    6. Add a descriptive text label using cv2.putText().
    7. Save and display the output image.

INPUT:
    white_canvas.jpg (Source image)

OUTPUT:
    experiment 33_output.jpg (Output image)

RESULT:
    Thus, a white image of custom dimensions with a drawn rectangle was successfully created using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

# Image dimensions
width, height = 600, 400
white_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define rectangle corners
pt1 = (100, 80)
pt2 = (500, 320)
color = (200, 50, 0) # Blue in BGR
thickness = 4

# Draw rectangle
cv2.rectangle(white_img, pt1, pt2, color, thickness)
cv2.putText(white_img, "Rectangle", (pt1[0] + 10, pt1[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

# Save and display
cv2.imwrite("experiment 33_output.jpg", white_img)
cv2.imshow("Rectangle on White Canvas", white_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Rectangle drawing complete.")

print("RESULT: Thus, a white image of custom dimensions with a drawn rectangle was successfully created using OpenCV.")
