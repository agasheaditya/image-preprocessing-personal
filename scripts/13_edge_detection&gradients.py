import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap:
    ret, frame = cap.read()
    if not ret:
        break
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    canny = cv2.Canny(frame, 100, 100)

    cv2.imshow("laplacian", laplacian)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)
    cv2.imshow("canny", canny)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
