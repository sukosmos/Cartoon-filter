import cv2
import numpy as np

def cartoonify(image_path):
    # Load the input image
    img = cv2.imread(image_path)
    
    # Apply bilateral filter to smooth colors while preserving edges
    color = cv2.bilateralFilter(img, 4, 100, 100)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise in the grayscale image
    gray_blur = cv2.medianBlur(gray, 5)

    # Detect edges using Canny edge detector, then thicken the edges using dilation
    edges = cv2.Canny(gray_blur, threshold1=700, threshold2=900, apertureSize=5)
    kernel = np.ones((3, 3), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)

    # Invert the edge image and use it as a mask to combine with the color image
    edges_inv = cv2.bitwise_not(edges_dilated)
    cartoon = cv2.bitwise_and(color, color, mask=edges_inv)

    # Increase brightness slightly to enhance cartoon effect (alpha: contrast, beta: brightness)
    cartoon = cv2.convertScaleAbs(cartoon, alpha=1.0, beta=10)

    # Show the final cartoonified image
    cv2.imshow("Cartoonified", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cartoonify("image.jpg")
