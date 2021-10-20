import cv2 as cv
import numpy as np
import random

# Get our camera
cam = cv.VideoCapture(0)

# Get our QR code detector
qrCodeDetector = cv.QRCodeDetector()

while True:
    # Get the frame from the camera
    ret, frame = cam.read()

    # Show the frame
    cv.imshow('frame', frame)
    
    # Check for QR code, if there is then decode it
    retval, decoded_info, points, straight_qrcode = qrCodeDetector.detectAndDecodeMulti(frame)

    # If there is at least 1 detected QR code
    if points is not None:
        # And we detect n QR codes
        if len(decoded_info) == 2:
            print(decoded_info)
    # Quit if q is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv.destroyAllWindows()