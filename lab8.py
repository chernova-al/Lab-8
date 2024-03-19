# var 7
import cv2
import time
import numpy as np
def z1():
    img = cv2.imread('variant-7.jpg')
    flipped = cv2.flip(img, 1)
    rotated = cv2.rotate(flipped, cv2.ROTATE_180)

    cv2.imshow('Rotated Image', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def z2_3():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    fly_img = cv2.imread('fly64.png') 
    fly_h, fly_w = fly_img.shape[:2]
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                distance = np.sqrt((320 - a) ** 2 + (240 - b) ** 2)
                print('Расстояние до центра равно: ',distance)

            start_x = int(a - fly_w / 2)
            start_y = int(b - fly_h / 2)
            frame[start_y:start_y+fly_h, start_x:start_x+fly_w] = fly_img

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()



