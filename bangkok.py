import cv2
import numpy as np

#Starting the webcam
video = cv2.VideoCapture(0)

# CREATE AN IMAGE VARIABLE 
image = cv2.imread("my pic.jpg")

#Reading the captured frame until the camera is open
while (True):
    ret, frame = video.read()
    if not ret:
        break
    #Use the code block to resize the image and frame
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
    #Use the code block to pass the faint shade value and dark shade value of RBG.
    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])
    #Code block to use inRange() and bitwise_and()
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    #Code block to use the where function.
    f = frame - res
    f = np.where(f == 0, image, f)
    #Show the real video and masked video.
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)
    #Break the loop if the user presses “Esc” or “Q”
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#Release the video and close the video windows.
video.release()
cv2.destroyAllWindows()


    