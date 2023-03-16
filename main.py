# Import Libraries
import cv2
from PIL import Image
from utils import get_limits #from external file we created

# Read Webcam
cap = cv2.VideoCapture(0)

# Insert Color code you want to detect
color = [255, 0, 0] #BGR color space

while True:
    ret, frame = cap.read()

    # Convert image reading from BGR to HSV
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # External function which gives lower & upper limit of a color choosen
    lowerLimit, upperLimit = get_limits(color)

    # Creates a Mask as black, and displays white color only when color we defined appears on screen
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask) #Creates an image memory from an object exporting the array interface
    bbox = mask_.getbbox() # Gets corner value of object for drawing bounding box

    # Bounding box will be drawn around object from values '.getbbox()'
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Displays output
    cv2.imshow('frame', frame)

    # Exit button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Releases the resources
cv2.destroyAllWindows()