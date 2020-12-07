#ADA: Automatic Dice acquisition
#NOTA: telecamera a 19 cm dal tavolo (altezza della lente)

import roll_counter
import time, cv2

#Setup options: DELAY_TIME being the time between one acquisition and the following

DELAY_TIME = 10
cap = cv2.VideoCapture(1)

#execute the loop, constantly acquiring an image and printing the total sum. DELAY_TIME between the acquisitions

while 1:
    count = roll_counter.count_dots(cap)
    print(count)
    time.sleep(DELAY_TIME)

#commento
cap.release()
