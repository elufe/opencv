
# coding: utf-8

# In[31]:


import cv2
import numpy as np
img1 = cv2.imread('C:/pill1.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('C:/pill2.jpg',cv2.IMREAD_COLOR)
img3 = cv2.imread('C:/pill3.jpg',cv2.IMREAD_COLOR)
img4 = cv2.imread('C:/pill4_1.jpg',cv2.IMREAD_COLOR)
img5 = cv2.imread('C:/pill5.jpg',cv2.IMREAD_COLOR)
img6 = cv2.imread('C:/pill6.jpg',cv2.IMREAD_COLOR)
img7 = cv2.imread('C:/pill7.jpg',cv2.IMREAD_COLOR)
img8 = cv2.imread('C:/pill8.jpg',cv2.IMREAD_COLOR)
img9 = cv2.imread('C:/pill9.jpg',cv2.IMREAD_COLOR)

yak1 = cv2.imread('C:/yak1.jpg',cv2.IMREAD_COLOR)
yak2 = cv2.imread('C:/yak2.jpg',cv2.IMREAD_COLOR)
yak3 = cv2.imread('C:/yak3.jpg',cv2.IMREAD_COLOR)
yak4 = cv2.imread('C:/yak4.jpg',cv2.IMREAD_COLOR)
yak5 = cv2.imread('C:/yak5.jpg',cv2.IMREAD_COLOR)
yak6 = cv2.imread('C:/yak6.jpg',cv2.IMREAD_COLOR)



saliency = cv2.saliency.StaticSaliencyFineGrained_create()

#(success, saliencyMap) = saliency.computeSaliency(img1)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img1, 3)
#cv2.imshow("input1", img1)
#cv2.medianBlur(saliencyMap, 3)
#cv2.imshow("output1", saliencyMap)
#cv2.medianBlur(threshMap, 3)
#cv2.imshow("thresh1", threshMap)

#(row,col,a) = img2.shape
#print(row)
#print(col)

#for i in range(col):
#    img2[120,i]=255
    


filter=5
    
yak11 = yak3[0:120,0:125]
yak12 = yak3[0:120,126:250]

yak113 = yak11

(success, saliencyMap) = saliency.computeSaliency(yak113)
threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(yak113, filter)
cv2.imshow("input113", yak113)
#cv2.medianBlur(saliencyMap, filter)
cv2.imshow("output113", saliencyMap)
cv2.medianBlur(threshMap, filter+4)
cv2.imshow("thresh113", threshMap)

#(success, saliencyMap) = saliency.computeSaliency(img2_2)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img2_2, filter)
#cv2.imshow("input2_2", img2_2)
#cv2.medianBlur(saliencyMap, filter)
#cv2.imshow("output2_2", saliencyMap)
#cv2.medianBlur(threshMap, filter)
#cv2.imshow("thresh2_2", threshMap)

#img3 = img3[0:120,0:250]    

#(success, saliencyMap) = saliency.computeSaliency(img3)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#(row,col,a) = img3.shape
#print(row)
#print(col)


#cv2.medianBlur(img3, filter)
#cv2.imshow("input3", img3)
#cv2.medianBlur(saliencyMap, filter)
#cv2.imshow("output3", saliencyMap)
#cv2.medianBlur(threshMap, filter)
#cv2.imshow("thresh3", threshMap)

#(success, saliencyMap) = saliency.computeSaliency(img4)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img4, 5)
#cv2.imshow("input4", img4)
#cv2.medianBlur(saliencyMap, 5)
#cv2.imshow("output4", saliencyMap)
#cv2.medianBlur(threshMap, 5)
#cv2.imshow("thresh4", threshMap)

#(success, saliencyMap) = saliency.computeSaliency(img5)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img5, 5)
#cv2.imshow("input5", img5)
#cv2.medianBlur(saliencyMap, 5)
##cv2.imshow("output5", saliencyMap)
##cv2.medianBlur(threshMap, 5)
#cv2.imshow("thresh5", threshMap)
#

#

filter=3

#(success, saliencyMap) = saliency.computeSaliency(img6#)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]#

#cv2.medianBlur(img6, filter#)
#cv2.imshow("input6", img6)
#cv2.medianBlur(saliencyMap, filter#)
#cv2.imshow("output6", saliencyMap)#
#cv2.medianBlur(threshMap, filter+10)
#cv2.imshow("thresh6", threshMap)

#(success, saliencyMap) = saliency.computeSaliency(img7)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img7, filter)
#cv2.imshow("input7", img7)
#cv2.medianBlur(saliencyMap, filter)
#cv2.imshow("output7", saliencyMap)
#cv2.medianBlur(threshMap, filter+10)
#cv2.imshow("thresh7", threshMap)

#(success, saliencyMap) = saliency.computeSaliency(img8)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img8, filter)
#cv2.imshow("input8", img8)
#cv2.medianBlur(saliencyMap, filter)
#cv2.imshow("output8", saliencyMap)
#cv2.medianBlur(threshMap, filter+10)
#cv2.imshow("thresh8", threshMap)

#(success, saliencyMap) = saliency.computeSaliency(img9)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(img9, filter)
#cv2.imshow("input9", img9)
#cv2.medianBlur(saliencyMap, filter)
#cv2.imshow("output9", saliencyMap)
#cv2.medianBlur(threshMap, filter+10)
#cv2.imshow("thresh9", threshMap)

cv2.waitKey(0)
cv2.destroyAllWindows()

