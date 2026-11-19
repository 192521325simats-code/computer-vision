"""
EXPERIMENT 34: Write a Python function to create a white image size entered by the user and then create a shape of Circle using Open CV.

AIM:
    To create a white image of custom dimensions and draw a circular geometric shape using OpenCV cv2.circle function.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Specify custom canvas dimensions (width=600, height=400).
    3. Create a blank white image using np.ones() * 255.
    4. Calculate circle center coordinates (width // 2, height // 2) and radius (120 pixels).
    5. Draw the circle outline using cv2.circle(image, center, radius, color, thickness).
    6. Mark the center point and add a text label.
    7. Save the resulting image and display the window.

INPUT:
    white_canvas.jpg (Source image)

OUTPUT:
    experiment 34_output.jpg (Output image)

RESULT:
    Thus, a white image with a centered geometric circle was successfully generated using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

# Image dimensions
width, height = 600, 400
white_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Circle center and radius
center = (width // 2, height // 2)
radius = 120
color = (0, 140, 255) # Orange in BGR
thickness = 4

# Draw circle and center point
cv2.circle(white_img, center, radius, color, thickness)
cv2.circle(white_img, center, 4, (0, 0, 255), -1)
cv2.putText(white_img, "Circle (Radius=120)", (center[0] - 100, center[1] + radius + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

# Save and display
cv2.imwrite("experiment 34_output.jpg", white_img)
cv2.imshow("Circle on White Canvas", white_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Circle drawing complete.")

print("RESULT: Thus, a white image with a centered geometric circle was successfully generated using OpenCV.")
