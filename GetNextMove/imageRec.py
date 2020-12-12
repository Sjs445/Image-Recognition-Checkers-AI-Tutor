import sys
import cv2 as cv
import numpy as np
from numpy.core.numeric import normalize_axis_tuple
import imutils
import imageio
import base64
import io 
from PIL import Image



#this function will test to see if the given xVal is within a column 
#if true it will return the column number. If false this will return -1
def findColumn(xVal):
    if(xVal > 230 and xVal < 554):
        return 0         
    elif(xVal > 554 and xVal < 878):
        return 1
    elif(xVal > 878 and xVal < 1202):
        return 2
    elif(xVal > 1202 and xVal < 1526):
        return 3
    elif(xVal > 1526 and xVal < 1850):
        return 4
    elif(xVal > 1850 and xVal < 2174):
        return 5
    elif(xVal > 2174 and xVal < 2498):
        return 6
    elif(xVal > 2498 and xVal < 2822):
        return 7
    else:
        return -1



def DetectImage(base64String):
    #path = r'C:\Users\btomi\OneDrive\Desktop\checkers2.jpg'
    # path = r'C:\Users\Shadow\Downloads\board.jpg'
    # image = cv.imread(path)
    # image2 = image.copy()
    #crop = image2[255:587,230:552]
    #crop = image2[919:1251,554:878]
    #cv.imshow('image',crop)
    #cv.waitKey(0)
    imgdata  = base64.b64decode(base64String)
    # image = np.array(Image.open(io.BytesIO(imgdata)))
    nparr = np.fromstring(imgdata, np.uint8)
    image = cv.imdecode(nparr, cv.IMREAD_COLOR)
    image2 = cv.imdecode(nparr, cv.IMREAD_COLOR)
    print(type(image))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    print(type(gray))

    #gray = cv.bilateralFilter(gray, 10, 15, 15)
    #edged = cv.Canny(gray, 30, 100)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1 , 100, minRadius = 60 , maxRadius=225)

    circles = np.round(circles[0, :]).astype("int")
    #print(len(circles))
    #cv.circle(image2, (216, 120), 45, (0, 255, 0), 4)
    #cv.imshow('image',gray)
    #cv.waitKey(0)

    temp = []
    if circles is not None:
        for c in circles:
            if c[2] > 130 and c[2] < 150:
                temp.append(c)
    circles = temp
    #creating 2D array 
    board_state = [ ['0']*8 for i in range(8)]
    #print(board_state)
    print(type(circles))

    # if len(circles) != 24:
    #     sys.exit("ERROR: detected too litte or too many circles than chips on board")


    #iterate through the circles found if they exist 
    if circles is not None:
        #circles = np.round(circles[0, :]).astype("int")
        row = -2 
        col = -2
        for (x, y, r) in circles:
            #find the row that the current circle resides
            #once we find the correct row we will find the 
            #corresponding column 
            #finally with the correct column and row 
            #we can insert a 1(for player 1) or 2(for player2)
            if(y > 255 and y < 587):
                col = findColumn(x)
                row = 0
            elif(y > 587 and y < 919):
                col = findColumn(x)
                row = 1
            elif(y > 919 and y < 1251):
                col = findColumn(x)
                row = 2
            elif(y > 1251 and y < 1583):
                col = findColumn(x)
                row = 3
            elif(y > 1583 and y < 1915):
                    col = findColumn(x)
                    row = 4
            elif(y > 1915 and y < 2247):
                    col = findColumn(x)
                    row = 5
            elif(y > 2247 and y < 2579):
                col = findColumn(x)
                row = 6
            elif(y > 2579 and y < 2911):
                col = findColumn(x)
                row = 7
            else:
                row = -1
            #thow exception if x value is not in range of possible positions 
            if(row != -1):
                #check to see if column is within the corresonding range 
                if(col != -1):
                    #if row and column are within range add value to 2D array 
                    #print("ROW:" , row)
                    #print("Col: ", col)
                    board_state[row][col] = 1
                    #still need to check if whether the checker is player 1 or player 2
                    print("coordinates X: ", x)
                    print("coordinates y: ", y)
                    print("BRG: ", image[y][x])
                    if image[y][x][2] > 130:
                            board_state[row][col] = 'R'
                    else:
                        board_state[row][col] = 'B'
                else:
                        print("ERROR: col val of circle was not within the range of the board")
            else:
                    print("ERROR: row value of circle was not within the range of the board")
        print("------------------------------------------------------------------------")
        print(board_state)
        #print(circles)
        #print(board_state)
        #print("BRG: ", image[796][522])


        # if circles is not None:
        # #circles = np.round(circles[0, :]).astype("int")
        #     for (x, y, r) in circles:
        #         cv.circle(image2, (x, y), r, (0, 255, 0), 4)
        #         cv.rectangle(image2, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)    

        # #cv.imshow("output", np.hstack([image, image2]))
        # #cv.imshow('image',image2)
        # #cv.waitKey(0)

        # OutputImageName=r'test.png'
        # imageio.imwrite(OutputImageName, image2)
        return board_state

######## Enable this section to load the test image to test this script only.###########
with open("image0.jpg", "rb") as image:
    f = image.read()
    b = bytearray(f)
    encoded = base64.b64encode(b)
    DetectImage(encoded)
########################################################################################

#for i in circles:
#    print(i)

#cv.circle(image2, (512, 418),44 , (0, 255, 0), 4)
#cv.rectangle(image2, (512, 418), (512 + 5, 418 + 5), (0, 128, 255), -1)
#cv.imshow("output", np.hstack([image, image2]))
#cv.imshow("test",image2[418:818,512:912])
#cv.waitKey(0)
"""
cnts = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(len(cnts))
#cnts = sorted(cnts, key = cv.contourArea, reverse = True)[3:200]
cnts = sorted(cnts, key = cv.contourArea, reverse = True)

print(type(cnts))
screenCnt = []
for c in cnts:
    peri = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.015 * peri, True)
    if len(approx) == 4:
    screenCnt.append(approx)

cv.drawContours(image, screenCnt, -1, (0, 255, 0), 3)
cv.imshow('image',image)
cv.waitKey(0)

#print("Spape: ", image.shape)
"""