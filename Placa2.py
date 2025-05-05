import cv2 as cv
import numpy as np 
import easyocr as ocr

img2 = cv.imread("/Users/danieledenwynter/Desktop/El arte de la programación/Actividad1/placa2.jpg")   

hsv2 = cv.cvtColor(img2, cv.COLOR_BGR2HSV)

lower_black = np.array([0, 0, 0]) 
upper_black = np.array([180, 255, 50]) 

mask2 = cv.inRange(hsv2, lower_black, upper_black)

average2 = cv.medianBlur(mask2, 5)
cv.imwrite("/Users/danieledenwynter/Desktop/El arte de la programación/Actividad1/placa_filtrada2.jpg", average2)

reader = ocr.Reader(["es"], gpu=False)
result2 = cv.imread("/Users/danieledenwynter/Desktop/El arte de la programación/Actividad1/placa_filtrada2.jpg")

result_text2 = reader.readtext(result2, paragraph=False)

for res in result_text2:
     print("res:", res)
     pt0 = res[0][0]
     pt1 = res[0][1]
     pt2 = res[0][2]
     pt3 = res[0][3]

     cv.rectangle(result2, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
     cv.putText(result2, res[1], (pt0[0], pt0[1] -3), 2, 0.8, (255, 255, 255), 1)

     cv.rectangle(result2, pt0, pt2, (166, 56, 242), 2)
     cv.circle(result2, pt0, 2, (255, 0, 0), 2)
     cv.circle(result2, pt1, 2, (0, 255, 0), 2)
     cv.circle(result2, pt2, 2, (0, 0, 255), 2)
     cv.circle(result2, pt3, 2, (0, 255, 255), 2)


     cv.imshow("Image", result2)
     cv.waitKey(0)
cv.destroyAllWindows()

