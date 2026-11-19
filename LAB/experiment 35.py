"""
EXPERIMENT 35: Write a Python function to create a text string entered by the user that must be appeared on the given image using Open CV.

AIM:
    To overlay a user-specified text string onto an existing input image at specified coordinates with customizable font, scale, and color using OpenCV cv2.putText.

PROCEDURE:
    1. Import cv2 and os.
    2. Read the source image from disk using cv2.imread().
    3. Define the text string entered by the user.
    4. Set text rendering parameters: font typeface (cv2.FONT_HERSHEY_SIMPLEX), origin coordinates (x, y), font scale, color (BGR), and line thickness.
    5. Render the text string onto the image using cv2.putText().
    6. Save the annotated image using cv2.imwrite() and display the output window.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 35_output.jpg (Output image)

RESULT:
    Thus, the user-entered text string was successfully overlaid onto the input image using OpenCV cv2.putText.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")
if image is None:
    raise FileNotFoundError("Input image photo.jpg not found.")

output = image.copy()
user_text = "COMPUTER VISION LAB - SIMATS"

# Text parameters
org = (50, 80)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.1
color = (0, 255, 255) # Yellow in BGR
thickness = 3

# Draw outline for contrast, then text
cv2.putText(output, user_text, (org[0] + 2, org[1] + 2), font, font_scale, (0, 0, 0), thickness + 2, cv2.LINE_AA)
cv2.putText(output, user_text, org, font, font_scale, color, thickness, cv2.LINE_AA)

# Save and display
cv2.imwrite("experiment 35_output.jpg", output)
cv2.imshow("Text on Image", output)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Text string overlay complete.")

print("RESULT: Thus, the user-entered text string was successfully overlaid onto the input image using OpenCV cv2.putText.")
