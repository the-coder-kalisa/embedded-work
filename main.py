import cv2
import pytesseract

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)

text = pytesseract.image_to_string(adaptive_result)

print(f"Text: {text}")