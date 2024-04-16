import cv2
import numpy as np
from matplotlib import pyplot as plt
import easyocr

cap = cv2.VideoCapture(0)
reader = easyocr.Reader(['en'], gpu=False)

while True:
    _, frame = cap.read()
    result = reader.readtext(frame)
    for detection in result:
        # Extract coordinates
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]
        print(text)
        # Draw rectangle
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow("Text Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
