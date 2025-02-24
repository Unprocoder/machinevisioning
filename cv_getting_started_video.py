import cv2
#* https://www.youtube.com/watch?v=-RtVZsCvXAQ&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=6

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FPS))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows