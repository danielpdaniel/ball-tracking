import cv2
import numpy

video = cv2.VideoCapture(0)
prevCircle = None
distance = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

while True:
    ret, frame = video.read()
    if not ret: break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (19,19), 0)

    circles = cv2.HoughCircles(blur_frame, cv2.HOUGH_GRADIENT, 1.2, 100, 
                               param1=100, param2=30, minRadius=75, maxRadius=400)
    
    if circles is not None:
        circles = numpy.uint16(numpy.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if distance(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= distance(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i

        # cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255), 3)
        prevCircle = chosen

    cv2.imshow(" ", frame)
    # cv2.imshow("frame", blur_frame)
    # cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
    # cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()