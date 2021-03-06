import cv2
import numpy as np
def cutout(img_file):
    IMAGE_FILE = img_file
    IMAGE_USER = IMAGE_FILE.replace(".jpg","").replace(".jpeg","").replace(".png","")
    print(IMAGE_USER)
    img = cv2.imread(IMAGE_FILE)
    #convert to YCrCb and filter
# old
#    lower = np.array([0,129,70], np.uint8)#yangxuanyue
#    #lower = np.array([0,139,70], np.uint8)#lihao
#    upper = np.array([255,180,127], np.uint8)
# new
    lower = np.array([0,131,102], np.uint8)#yangxuanyue
    upper = np.array([255,183,154], np.uint8)
	
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    mask = cv2.inRange(ycrcb, lower, upper)
#    skin = cv2.bitwise_and(img, img, mask=mask)
#    cv2.imwrite("{0}_skin.jpg".format(IMAGE_USER),skin)

    kernel = np.ones((57,57),np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    skin = cv2.bitwise_and(img, img, mask=opening)
    cv2.imwrite("{0}_skin.jpg".format(IMAGE_USER),skin)

    _,black_and_white = cv2.threshold(opening, 127,255,0)
    #find max contours
    _, contours, _ = cv2.findContours(black_and_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    length = len(contours)
    maxArea = -1
    final_Contour = np.zeros(img.shape, np.uint8)
    if length > 0:
        for i in range(length):
            temp = contours[i]
            area = cv2.contourArea(temp)
            if area > maxArea:
                maxArea = area
                ci = i
        largest_contour = contours[ci]
    cv2.drawContours(final_Contour, [largest_contour], 0, (0, 255, 0), 10)
    cv2.imwrite("{0}_contour.jpg".format(IMAGE_USER),final_Contour)
    cv2.drawContours(skin, [largest_contour], 0, (0, 255, 0), 10)
    cv2.imwrite("{0}_contour_skin.jpg".format(IMAGE_USER),skin)

if __name__ == '__main__':
#    cutout("../image/yangxuanyue/yangxuanyue.jpg")
    cutout("../image/lihao/lihao.jpg")
