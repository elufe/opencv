
# coding: utf-8

# In[18]:


import cv2
import numpy as np
img1 = cv2.imread('C:/pill/pill1.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('C:/pill/pill2.jpg',cv2.IMREAD_COLOR)
img3 = cv2.imread('C:/pill/pill3.jpg',cv2.IMREAD_COLOR)
img4 = cv2.imread('C:/pill/pill4_1.jpg',cv2.IMREAD_COLOR)
img5 = cv2.imread('C:/pill/pill5.jpg',cv2.IMREAD_COLOR)
img6 = cv2.imread('C:/pill/pill6.jpg',cv2.IMREAD_COLOR)
img7 = cv2.imread('C:/pill/pill7.jpg',cv2.IMREAD_COLOR)
img8 = cv2.imread('C:/pill/pill8.jpg',cv2.IMREAD_COLOR)
img9 = cv2.imread('C:/pill/pill9.jpg',cv2.IMREAD_COLOR)
img10 = cv2.imread('C:/pill/pill10.jpg',cv2.IMREAD_COLOR)
img11 = cv2.imread('C:/pill/pill11.jpg',cv2.IMREAD_COLOR)
img12 = cv2.imread('C:/pill/pill12.jpg',cv2.IMREAD_COLOR)
img13 = cv2.imread('C:/pill/pill13.jpg',cv2.IMREAD_COLOR)
img14 = cv2.imread('C:/pill/pill14.jpg',cv2.IMREAD_COLOR)
img15 = cv2.imread('C:/pill/pill15.jpg',cv2.IMREAD_COLOR)
img16 = cv2.imread('C:/pill/pill16.jpg',cv2.IMREAD_COLOR)

yak1 = cv2.imread('C:/pill/yak1.jpg',cv2.IMREAD_COLOR)
yak2 = cv2.imread('C:/pill/yak2.jpg',cv2.IMREAD_COLOR)
yak3 = cv2.imread('C:/pill/yak3.jpg',cv2.IMREAD_COLOR)
yak4 = cv2.imread('C:/pill/yak4.jpg',cv2.IMREAD_COLOR)
yak5 = cv2.imread('C:/pill/yak5.jpg',cv2.IMREAD_COLOR)
yak6 = cv2.imread('C:/pill/yak6.jpg',cv2.IMREAD_COLOR)

pilll = cv2.imread('C:/pilll.jpg',cv2.IMREAD_COLOR)


#saliency 생성
saliency = cv2.saliency.StaticSaliencyFineGrained_create()


#약학정보원 사진 절반 나누기    
yak11 = yak4[0:120,0:125]
yak12 = yak4[0:120,126:250]


# 약 설정
imgx = img16
#saliencyMap 생성, thresMap생성(otsu threshold)
(success, saliencyMap) = saliency.computeSaliency(imgx)
threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]




#cv2.medianBlur(img6, filter)
cv2.imshow("inputx", imgx)
#cv2.medianBlur(saliencyMap, filter)
cv2.imshow("outputx", saliencyMap)
cv2.medianBlur(threshMap, 3)
cv2.imshow("threshx", threshMap)




#hsv로 변환후 v가 0.5이하면 그림자로 취급 검은색으로 만듬
hsv = cv2.cvtColor(imgx, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

(row,col) = v.shape
print(row)
print(col)

#최대 v 최소v 찾고 0에서 1로 정규화
max = v[0][0]
min = v[0][0]
for i in range(row):
    for j in range(col):
        if (max<v[i][j]) :
            max = v[i][j];
        elif (min > v[i][j]) :
            min = v[i][j]

# 그림자 제거            
for i in range(row):
    for j in range(col):
        x = (v[i][j]-min)/((max-min)+1e-10)
        if(x<=0.6) :
            threshMap[i][j]=0

# 필터적용            
#cv2.medianBlur(threshMap, 11)
threshMap = cv2.GaussianBlur(threshMap, (7,7), 0)
threshMap = cv2.GaussianBlur(threshMap, (7,7), 0)


for i in range(row):
    for j in range(col):
        if (threshMap[i][j]==0) :
            imgx[i][j]=0
            


cv2.imshow("threshx_filter", threshMap)


#가운데 기준으로 흰색 경계부분 검출
(row,col,a) = imgx.shape
right = (int)(col/2)
left = (int)(col/2)
up = (int)(row/2)+0
down = (int)(row/2)+0
print(imgx[up][left])
print(right)
print(left)
check=1
L=[0,0,0]



for i in range(int(row/2),row):
    for j in range(int(col/2),col):
        if(threshMap[i][j] == 0):
            if(right<j):
                right = j
            break
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


#정사각형으로 조절            
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
            
#알약부분 추출
if((down-up)>(right-left)) :
    a = int(((down-up)-(right-left))/2)
    right=right+a
    left=left-a
    b = row-1
else:
    a = int(((right-left)-(down-up))/2)
    down=down+a
    up=up-a
    b = col-1

    
#for i in range(b):
#    imgx[i][left]=255
#    imgx[i][right]=255
#for i in range(b):
#    imgx[up][i]=255
#    imgx[down][i]=255

print(up)
print(down)
print(left)
print(right)

#이미지 저장
aaa = threshMap[up:down,left:right]    
print(aaa.shape)
print(aaa.shape)
cv2.imshow("imgx",aaa)

cv2.imwrite("C:/Download/aaa10.jpg", aaa);
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




cv2.waitKey(0)
cv2.destroyAllWindows()

