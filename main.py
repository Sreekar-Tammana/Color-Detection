import cv2
from PIL import Image
from utils import get_limits

cap = cv2.VideoCapture(0)
color = [255, 0, 0] #BGR color space

while True:
    ret, frame = cap.read()

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color)

    # ll1, ll2, ll3 = lowerLimit[0], lowerLimit[1], lowerLimit[2]
    # ul1, ul2, ul3 = upperLimit[0], upperLimit[1], upperLimit[2]

    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()