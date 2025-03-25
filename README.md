# Cartooon-filter
Make your picture like a cartoon!
This project applies cartoon-style filters to your images using **OpenCV**.

<br><br>

## **Basic Features**

### **1. Bilateral Filter for Smooth Colors**

```python
color = cv2.bilateralFilter(img, 4, 100, 100)
```

- Softens the color regions while keeping edge lines clear.
- Gives the image a painted or hand-drawn look.

<br><br>

### **2. Convert to Grayscale**

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

- Converts the image to grayscale for edge detection.

<br><br>

### **3. Noise Reduction with Median Blur**

```python
gray_blur = cv2.medianBlur(gray, 5)
```

- Smooths out small noise in the grayscale image.

<br><br>

### **4. Edge Detection (Canny + Dilation)**

```python
edges = cv2.Canny(gray_blur, 700, 900, apertureSize=5)
edges_dilated = cv2.dilate(edges, kernel, iterations=1)
```

- Detects strong edges, then thickens them for a cartoon-style outline.

<br><br>

### **5. Combine Edges with Color Image**

```python
edges_inv = cv2.bitwise_not(edges_dilated)
cartoon = cv2.bitwise_and(color, color, mask=edges_inv)

```

- Combines the inverted edge mask with the color-filtered image.

<br><br>

### **6. Brightness & Contrast Enhancement**

```python
cartoon = cv2.convertScaleAbs(cartoon, alpha=1.0, beta=10)
```

- Enhances the final result with brightness&contrast.

<br><br>

## 🖼️ Example Output

<p align="center">
  <img src = "https://github.com/user-attachments/assets/2f49aad0-7606-4ad2-9f16-7339451f6d34" width="40%" height="40%">  
  <img src = "https://github.com/user-attachments/assets/167ad3a2-dbd2-4b55-9803-a20eec540d2a" width="40%" height="40%">
</p>


<p align="center">
  <img src = "https://github.com/user-attachments/assets/5f3e444e-7e24-45cf-86a7-f6a9f52f9a38" width="40%" height="40%">  
  <img src = "https://github.com/user-attachments/assets/71941d2e-11d5-4ce5-9f70-de49dbf49e27" width="40%" height="40%">
</p>

<br><br>

---

*For Computer Vision*
