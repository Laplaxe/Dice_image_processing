from PIL import Image
import cv2

#PERCENTAGE: % of pixels in the subregion examined recquired to consider the region a dot
#DIAMETER: pixel number of the dot's DIAMETER
#MAX_X,MAX_Y number of pixel the image is rescaled to (ex, from 1080x720 to MAX_XxMAX_Y)
#MIN_WHITE_BRIGHTNESS: minimum brightness of a pixel for it to be considered white
#BLACK_BRIGHTNESS: brightness od black pixels

PERCENTAGE = 0.7
DIAMETER = 8
MAX_X, MAX_Y = 300, 300

MIN_WHITE_BRIGHTNESS = 100
BLACK_BRIGHTNESS = 0

#Acquire an image from the webcam, make it greyscale and resize it

def acquire_image(cap):
    ret, frame = cap.read()
    if not ret:
        raise FileNotFoundError
    dice = Image.fromarray(frame).convert("L").resize((MAX_X,MAX_Y))
    dice.show()
    return dice

#check wheter the subimage starting at i,j is a dot. In this case, make it all black and return 1. Otherwise, return 0.

def check_sub_image(dice, i, j):
    black_px = 0
    result = 0
    for m in range(0, DIAMETER):
        for n in range(0, DIAMETER):
            if dice.getpixel((n+i,m+j)) >= MIN_WHITE_BRIGHTNESS:
                black_px+=1
    if black_px >= PERCENTAGE*DIAMETER**2:
        result = 1
        for m in range(0, DIAMETER):
            for n in range(0, DIAMETER):
                dice.putpixel((n+i,m+j), BLACK_BRIGHTNESS)
    return result

#acquire the image and count the dots. Return the number of dots

def count_dots(cap):
    number_count = 0
    dice = acquire_image(cap)
    for j in range(0, MAX_Y-DIAMETER,2):
        for i in range(0,MAX_X-DIAMETER,2):
            number_count += check_sub_image(dice, i, j)
    dice.show()
    return(number_count)



if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    count_dots(cap)
    cap.release()
