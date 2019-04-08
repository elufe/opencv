
# coding: utf-8

# In[1]:


import cv2
import numpy as np
img1 = cv2.imread('C:/pill/pill1.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('C:/pill/pill2.jpg',cv2.IMREAD_COLOR)
img3 = cv2.imread('C:/pill/pill3.jpg',cv2.IMREAD_COLOR)
img4 = cv2.imread('C:/pill/pill4_1.jpg',cv2.IMREAD_COLOR)
img5 = cv2.imread('C:/pill/pill5.jpg',cv2.IMREAD_COLOR)
img6 = cv2.imread('C:/pill/pill6_1.jpg',cv2.IMREAD_COLOR)
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
img17 = cv2.imread('C:/pill/pill17.jpg',cv2.IMREAD_COLOR)
img18 = cv2.imread('C:/pill/pill18.jpg',cv2.IMREAD_COLOR)
img19 = cv2.imread('C:/pill/pill19.jpg',cv2.IMREAD_COLOR)
img20 = cv2.imread('C:/pill/pill20.jpg',cv2.IMREAD_COLOR)
#img21 = cv2.imread('C:/pill/pill21.jpg',cv2.IMREAD_COLOR)
#img22 = cv2.imread('C:/pill/pill22.jpg',cv2.IMREAD_COLOR)
#img23 = cv2.imread('C:/pill/pill23.jpg',cv2.IMREAD_COLOR)
#img24 = cv2.imread('C:/pill/pill24.jpg',cv2.IMREAD_COLOR)
#img25 = cv2.imread('C:/pill/pill25.jpg',cv2.IMREAD_COLOR)

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
yak11 = yak2[0:120,0:125]
yak12 = yak2[0:120,126:250]


# 약 설정
imgx = img5
imglast = imgx.copy()
#imgx = cv2.cvtColor(imgx, cv2.COLOR_BGR2Lab)
#cv2.imshow("lab",imgx)

cv2.pyrMeanShiftFiltering(imgx, 2, 10, imgx, 4)

cv2.imshow("origin",imgx)


def backproject(source, target, levels = 2, scale = 1):
        hsv = cv2.cvtColor(source,  cv2.COLOR_BGR2HSV)
        hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
        # calculating object histogram
        roihist = cv2.calcHist([hsv],[0, 1], None,             [levels, levels], [0, 180, 0, 256] )

        # normalize histogram and apply backprojection
        cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
        dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256], scale)
        return dst

backproj = np.uint8(backproject(imgx, imgx, levels = 2))
backproj = 255 - backproj
cv2.imshow("img2",backproj)





cv2.normalize(backproj,backproj,0,255,cv2.NORM_MINMAX)

saliencies = [backproj, backproj, backproj]
saliency = cv2.merge(saliencies)


cv2.pyrMeanShiftFiltering(saliency, 20, 200, saliency, 2)
saliency = cv2.cvtColor(saliency, cv2.COLOR_BGR2GRAY)
cv2.imshow("img13",saliency)

#cv2.equalizeHist(saliency, saliency)
#cv2.imshow("img12",saliency)
saliencyMap = saliency

cv2.imshow("saliency",saliency)


#saliencyMap 생성, thresMap생성(otsu threshold)
#(success, saliencyMap) = saliency.computeSaliency(imgx)


threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#(T, aaa) = cv2.threshold(saliency, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("thres",threshMap)

#hsv로 변환후 v가 0.5이하면 그림자로 취급 검은색으로 만듬
hsv = cv2.cvtColor(imgx, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

(row,col) = v.shape


#최대 v 최소v 찾고 0에서 1로 정규화
max = v[0][0]
min = v[0][0]

ave=0
cnt=0

for i in range(row):
    for j in range(col):
        ave+=v[i][j]
        cnt+=1
        if (max<v[i][j]) :
            max = v[i][j];
        elif (min > v[i][j]) :
            min = v[i][j]




# 그림자 제거            

for i in range(row):
    for j in range(col):
        x = (v[i][j]-min)/((max-min)+1e-10)
        if(x<=0.5) :
            threshMap[i][j] = 0
            imgx[i][j]=0
            imglast[i][j]=0


for i in range(row):
    for j in range(col):
        if (threshMap[i][j]==0) :
            imgx[i][j]=0
            imglast[i][j]=0

            
cv2.imshow("shadow",threshMap)

            
#가운데 기준으로 흰색 경계부분 검출
(row,col,a) = imgx.shape
right = (int)(col/2)
left = (int)(col/2)
up = (int)(row/2)+0
down = (int)(row/2)+0
print(imgx[up][left])
print(right)
print(left)
check=0
L=[0,0,0]


for i in range(int(row/2),row):
    for j in range(int(col/2),col-5):
        if((threshMap[i][j+1]+threshMap[i][j+2]+threshMap[i][j+3]+threshMap[i][j+4]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            break
        else:    
            threshMap[i][j]=255
    check=0        
    for j in range(int(col/2),5,-1):
        if((threshMap[i][j-1]+threshMap[i][j-2]+threshMap[i][j-3]+threshMap[i][j-4]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            
            break
        else:    
            threshMap[i][j]=255
    check=0       

for i in range(int(row/2),0,-1):
    for j in range(int(col/2),col-5):
        if((threshMap[i][j+1]+threshMap[i][j+2]+threshMap[i][j+3]+threshMap[i][j+4]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            
            break
        else:    
            threshMap[i][j]=255
    check=0
            
    for j in range(int(col/2),5,-1):
        if((threshMap[i][j-1]+threshMap[i][j-2]+threshMap[i][j-3]+threshMap[i][j-4]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            
            break
        else:    
            threshMap[i][j]=255
    check=0
            
for j in range(int(col/2),col):
    for i in range(int(row/2),row-5):
        if((threshMap[i+1][j]+threshMap[i+2][j]+threshMap[i+3][j]+threshMap[i+4][j]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            
            break
        else:    
            threshMap[i][j]=255
    check=0
    for i in range(int(row/2),5,-1):
        if((threshMap[i-1][j]+threshMap[i-2][j]+threshMap[i-3][j]+threshMap[i-4][j]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            
            break
        else:    
            threshMap[i][j]=255
    check=0 
            
for j in range(int(col/2),0,-1):
    for i in range(int(row/2),row-5):
        if((threshMap[i+1][j]+threshMap[i+2][j]+threshMap[i+3][j]+threshMap[i+4][j]) < 10):
#            threshMap[i][j]=255
            check=check+1
        if(check>0):
            
            break
        else:    
            threshMap[i][j]=255
    check=0
    for i in range(int(row/2),5,-1):
        if((threshMap[i-1][j]+threshMap[i-2][j]+threshMap[i-3][j]+threshMap[i-4][j]) < 10):
#            threshMap[i][j] = 255
            check=check+1
        if(check>0):
            break
        else:    
            threshMap[i][j]=255
            
threshMap = cv2.GaussianBlur(threshMap, (7,7), 0)            
cv2.imshow("fill",threshMap)

#------------------------------------------------------------------------------------------------------------------------------

image,contours, hierarchy = cv2.findContours(threshMap * 1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea)
#        image = cv2.drawContours(imgx, contours, -1, (0,255,255), 3)
#        cv2.imshow("1",image)
for i in range(-1,2): 
    x,y,w,h = cv2.boundingRect(contours[i])
    if x<(col/2) and (x+w)>(col/2) and y<(row/2) and (y+h)>(row/2):
        break;
    print(i)
#x,y,w,h = cv2.boundingRect(contours[0])
image = cv2.drawContours(threshMap, contours, -1, (0,255,0), 3)
cv2.imshow("line",image)
cv2.rectangle(imgx,(x,y),(x+w,y+h),(255,255,255),2)
print(x,y,w,h)
aaa = threshMap[y:y+h,x:x+w]
bbb = imglast[y:y+h,x:x+w]
cv2.imshow("2",aaa)
cv2.imshow("3",bbb)



    


cv2.imwrite("C:/Download/aaa10.jpg", bbb);





cv2.waitKey(0)
cv2.destroyAllWindows()

