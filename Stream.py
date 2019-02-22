import cv2
cap =  cv2.VideoCapture(0)

while True: 
    _, img = cap.read()
    cv2.imshow('frame',img)
    cv2.imshow('frame2',crop_img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()