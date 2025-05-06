import numpy as np 
import easyocr as ocr

import cv2 as cv

# Load the average
img = cv.imread("/Users/danieledenwynter/Desktop/El arte de la programación/Actividad1/placa.jpg")

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define HSV range for yellow
lower_black = np.array([0, 0, 0]) 
upper_black = np.array([180, 255, 50]) 

# Create a mask
mask = cv.inRange(hsv, lower_black, upper_black)

# Apply avg filter
average = cv.medianBlur(mask, 5)

# Ocr language and reader
reader = ocr.Reader(["es"], gpu=False)
result = cv.imread("/Users/danieledenwynter/Desktop/El arte de la programación/Actividad1/placa_filtrada.jpg")

# Display the result
result_text = reader.readtext(result, paragraph=False)

for res in result_text:
     print("res:", res)
     pt0 = res[0][0]
     pt1 = res[0][1]
     pt2 = res[0][2]
     pt3 = res[0][3]

     cv.rectangle(result, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
     cv.putText(result, res[1], (pt0[0], pt0[1] -3), 2, 0.8, (255, 255, 255), 1)

     cv.rectangle(result, pt0, pt2, (166, 56, 242), 2)
     cv.circle(result, pt0, 2, (255, 0, 0), 2)
     cv.circle(result, pt1, 2, (0, 255, 0), 2)
     cv.circle(result, pt2, 2, (0, 0, 255), 2)
     cv.circle(result, pt3, 2, (0, 255, 255), 2)


     cv.imshow("Image", result)
     cv.waitKey(0)
cv.destroyAllWindows()
