import cv2
#* https://www.youtube.com/watch?v=-RtVZsCvXAQ&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=6

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows