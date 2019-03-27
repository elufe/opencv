
# coding: utf-8

# In[4]:


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

pilll = cv2.imread('C:/pilll.jpg',cv2.IMREAD_COLOR)


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
    


#filter=5
    
#yak11 = yak1[0:120,0:125]
#yak12 = yak1[0:120,126:250]

#yak113 = yak11

#(success, saliencyMap) = saliency.computeSaliency(yak113)
#threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.medianBlur(yak113, filter)
#cv2.imshow("input113", yak113)
#cv2.medianBlur(saliencyMap, filter)
#cv2.imshow("output113", saliencyMap)
#cv2.medianBlur(threshMap, filter+4)
#cv2.imshow("thresh113", threshMap)

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


filter=3

imgx = img6;

(success, saliencyMap) = saliency.computeSaliency(imgx)
threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]




#cv2.medianBlur(img6, filter)
cv2.imshow("inputx", imgx)
#cv2.medianBlur(saliencyMap, filter)
cv2.imshow("outputx", saliencyMap)
cv2.medianBlur(threshMap, 3)
cv2.imshow("threshx", threshMap)





hsv = cv2.cvtColor(imgx, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

(row,col) = v.shape
print(row)
print(col)

max = v[0][0]
min = v[0][0]
for i in range(row):
    for j in range(col):
        if (max<v[i][j]) :
            max = v[i][j];
        elif (min > v[i][j]) :
            min = v[i][j]

for i in range(row):
    for j in range(col):
        x = (v[i][j]-min)/((max-min)+1e-10)
        if(x<=0.6) :
            threshMap[i][j]=0

            
#cv2.medianBlur(threshMap, 11)
threshMap = cv2.GaussianBlur(threshMap, (7,7), 0)
threshMap = cv2.GaussianBlur(threshMap, (7,7), 0)


for i in range(row):
    for j in range(col):
        if (threshMap[i][j]==0) :
            imgx[i][j]=0
            
for i in range(int(row/2),row):
    if(np.array_equal(imgx[i][(int)(col/2)],[0,0,0])):
        print(i)
        break;

for i in range(int(col/2),col):
    if(np.array_equal(imgx[(int)(row/2)+30][j],[0,0,0])):
        print(j)
        break;

cv2.imshow("threshx_filter", threshMap)



(row,col,a) = imgx.shape
right = (int)(col/2)
left = (int)(col/2)
up = (int)(row/2)+30
down = (int)(row/2)+30
print(imgx[up][left])
print(right)
print(left)
check=1
L=[0,0,0]





for i in range(int(row/2),row):
#    print("i="+str(i))
    for j in range(int(col/2),col):
        if(threshMap[i][j] == 0):
           # print("-----------------------------------------------------")
            if(right<j):
                right = j
            break
#    check=1
    for j in range(int(col/2),0,-1):
        if(threshMap[i][j] == 0):
            if(left>j):
                left = j
            break

            

for i in range(int(row/2),0,-1):
    for j in range(int(col/2),col):
        if(threshMap[i][j] == 0):
          #  print(j)
            if(right<j):
                right = j
            break

    for j in range(int(col/2),0,-1):
        if(threshMap[i][j] == 0):
            if(left>j):
                left = j
            break

for j in range(int(col/2),col):
    for i in range(int(row/2),row):
        if(threshMap[i][j] == 0):
            if(down<i):
                down = i
            break

    for i in range(int(row/2),0,-1):
        if(threshMap[i][j] == 0):
            if(up>i):
                up = i
            break


for j in range(int(col/2),col,-1):
    for i in range(int(row/2),row):
        if(threshMap[i][j] == 0):
            if(down<i):
                down = i
            break

    for i in range(int(row/2),0,-1):
        if(threshMap[i][j] == 0):
            if(up>i):
                up = i
            break


print(up)
print(down)
print(left)
print(right)

for i in range(row-1):
    imgx[i][left]=255
    imgx[i][right]=255
for i in range(col-1):
    imgx[up][i]=255
    imgx[down][i]=255

imgx = imgx[up:down,left:right]    
cv2.imshow("imgx",imgx)

#-------------------------------------------------------------------------------------------           

#원본파일로 해보고 안되면 이진파일로 해볼것
#image, contours, hierachy = cv2.findContours(threshMap, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

#print(hierachy)
#a=len(hierachy[0])
#print(a)
#print(contours[a-1])


#image,contours,hierachy=cv2.findContours(imgx,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#image = cv2.drawContours(image, contours[a-1], -1, (100,100,255), 3)
#image = cv2.drawContours(image, contours[a-2], -1, (100,100,255), 3)


#print(contours[6])

#cv2.imshow("countour",image)
            
        
#cv2.imshow("v",v)
#cv2.imshow("hsv",v)
#cv2.medianBlur(threshMap,9)
#cv2.imwrite("C:/Download/pill_good.jpg", threshMap);
#cv2.imshow("treshx_hsv",threshMap)


#---------------------------------------------------------------------------------------------



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

