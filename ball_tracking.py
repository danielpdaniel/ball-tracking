import cv2
# import numpy

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret: break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (19,19), 0)

    cv2.imshow("frame", blur_frame)
    # cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
    # cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()