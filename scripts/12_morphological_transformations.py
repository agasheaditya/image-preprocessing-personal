import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150, 0, 0])
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    ### Erosion and dilation
    kernel = np.ones((5, 5), dtype=np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    
    cv2.imshow("real video", frame)
    cv2.imshow("res video", res)
    # cv2.imshow("erosion video", erosion)
    # cv2.imshow("dilation video", dilation)
    # cv2.imshow("opening video", opening)
    # cv2.imshow("closing video", closing)
    cv2.imshow("tophat video", tophat)
    cv2.imshow("blackhat video", blackhat)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
