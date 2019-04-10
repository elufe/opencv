
# coding: utf-8

# In[14]:


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
img21 = cv2.imread('C:/pill/pill21.jpg',cv2.IMREAD_COLOR)
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


pill1 = cv2.imread('C:/pill/pill (1).jpg',cv2.IMREAD_COLOR)
pill2 = cv2.imread('C:/pill/pill (2).jpg',cv2.IMREAD_COLOR)
pill3 = cv2.imread('C:/pill/pill (3).jpg',cv2.IMREAD_COLOR)
pill4 = cv2.imread('C:/pill/pill (4).jpg',cv2.IMREAD_COLOR)
pill5 = cv2.imread('C:/pill/pill (5).jpg',cv2.IMREAD_COLOR)#파란색부분만 나옴
pill6 = cv2.imread('C:/pill/pill (6).jpg',cv2.IMREAD_COLOR)#반대로 나옴
pill7 = cv2.imread('C:/pill/pill (7).jpg',cv2.IMREAD_COLOR)
pill8 = cv2.imread('C:/pill/pill (8).jpg',cv2.IMREAD_COLOR)
pill9 = cv2.imread('C:/pill/pill (9).jpg',cv2.IMREAD_COLOR)
pill10 = cv2.imread('C:/pill/pill (10).jpg',cv2.IMREAD_COLOR)
pill11 = cv2.imread('C:/pill/pill (11).jpg',cv2.IMREAD_COLOR)
pill12 = cv2.imread('C:/pill/pill (12).jpg',cv2.IMREAD_COLOR)
pill13 = cv2.imread('C:/pill/pill (13).jpg',cv2.IMREAD_COLOR)
pill14 = cv2.imread('C:/pill/pill (14).jpg',cv2.IMREAD_COLOR)
pill15 = cv2.imread('C:/pill/pill (15).jpg',cv2.IMREAD_COLOR)
pill16 = cv2.imread('C:/pill/pill (16).jpg',cv2.IMREAD_COLOR)
pill17 = cv2.imread('C:/pill/pill (17).jpg',cv2.IMREAD_COLOR)
pill18 = cv2.imread('C:/pill/pill (18).jpg',cv2.IMREAD_COLOR)
pill19 = cv2.imread('C:/pill/pill (19).jpg',cv2.IMREAD_COLOR)
pill20 = cv2.imread('C:/pill/pill (20).jpg',cv2.IMREAD_COLOR)
pill21 = cv2.imread('C:/pill/pill (21).jpg',cv2.IMREAD_COLOR)
pill22 = cv2.imread('C:/pill/pill (22).jpg',cv2.IMREAD_COLOR)
pill23 = cv2.imread('C:/pill/pill (23).jpg',cv2.IMREAD_COLOR)
pill24 = cv2.imread('C:/pill/pill (24).jpg',cv2.IMREAD_COLOR)

croll1 = cv2.imread('C:/pill/croll1.jpg',cv2.IMREAD_COLOR)
croll2 = cv2.imread('C:/pill/croll2.jpg',cv2.IMREAD_COLOR)
croll3 = cv2.imread('C:/pill/croll3.jpg',cv2.IMREAD_COLOR)
croll4 = cv2.imread('C:/pill/croll4.jpg',cv2.IMREAD_COLOR)
croll5 = cv2.imread('C:/pill/croll5.jpg',cv2.IMREAD_COLOR)
croll6 = cv2.imread('C:/pill/croll6.jpg',cv2.IMREAD_COLOR)
croll7 = cv2.imread('C:/pill/croll7.jpg',cv2.IMREAD_COLOR)
croll8 = cv2.imread('C:/pill/croll8.jpg',cv2.IMREAD_COLOR)
croll9 = cv2.imread('C:/pill/croll9.jpg',cv2.IMREAD_COLOR)
croll10 = cv2.imread('C:/pill/croll10.jpg',cv2.IMREAD_COLOR)
croll11 = cv2.imread('C:/pill/croll11.jpg',cv2.IMREAD_COLOR)
croll12 = cv2.imread('C:/pill/croll12.jpg',cv2.IMREAD_COLOR)
croll13 = cv2.imread('C:/pill/croll13.jpg',cv2.IMREAD_COLOR)
croll14 = cv2.imread('C:/pill/croll14.jpg',cv2.IMREAD_COLOR)
croll15 = cv2.imread('C:/pill/croll15.jpg',cv2.IMREAD_COLOR)
croll16 = cv2.imread('C:/pill/croll16.jpg',cv2.IMREAD_COLOR)
croll17 = cv2.imread('C:/pill/croll17.jpg',cv2.IMREAD_COLOR)
croll18 = cv2.imread('C:/pill/croll18.jpg',cv2.IMREAD_COLOR)
croll19 = cv2.imread('C:/pill/croll19.jpg',cv2.IMREAD_COLOR)
croll20 = cv2.imread('C:/pill/croll20.jpg',cv2.IMREAD_COLOR)
croll21 = cv2.imread('C:/pill/croll21.jpg',cv2.IMREAD_COLOR)
croll22 = cv2.imread('C:/pill/croll22.jpg',cv2.IMREAD_COLOR)
croll23 = cv2.imread('C:/pill/croll23.jpg',cv2.IMREAD_COLOR)
croll24 = cv2.imread('C:/pill/croll24.jpg',cv2.IMREAD_COLOR)
croll25 = cv2.imread('C:/pill/croll25.jpg',cv2.IMREAD_COLOR)
croll26 = cv2.imread('C:/pill/croll26.jpg',cv2.IMREAD_COLOR)
croll27 = cv2.imread('C:/pill/croll27.jpg',cv2.IMREAD_COLOR)
croll28 = cv2.imread('C:/pill/croll28.jpg',cv2.IMREAD_COLOR)
croll29 = cv2.imread('C:/pill/croll29.jpg',cv2.IMREAD_COLOR)
croll30 = cv2.imread('C:/pill/croll30.jpg',cv2.IMREAD_COLOR)
croll31 = cv2.imread('C:/pill/croll31.jpg',cv2.IMREAD_COLOR)
croll32 = cv2.imread('C:/pill/croll32.jpg',cv2.IMREAD_COLOR)
croll33 = cv2.imread('C:/pill/croll33.jpg',cv2.IMREAD_COLOR)
croll34 = cv2.imread('C:/pill/croll34.jpg',cv2.IMREAD_COLOR)
croll35 = cv2.imread('C:/pill/croll35.jpg',cv2.IMREAD_COLOR)
croll36 = cv2.imread('C:/pill/croll36.jpg',cv2.IMREAD_COLOR)



baek1 = cv2.imread('C:/pill/baek1.jpg',cv2.IMREAD_COLOR)
baek2 = cv2.imread('C:/pill/baek2.jpg',cv2.IMREAD_COLOR)
baek3 = cv2.imread('C:/pill/baek3.jpg',cv2.IMREAD_COLOR)


#약학정보원 사진 절반 나누기 
croll = croll5
yak = croll[0:120,0:125]
yakk = croll[0:120,126:250]



# 약 설정
imgx = croll3#croll21[0:370,0:780]
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


saliencyMap = saliency

cv2.imshow("saliency",saliency)




threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

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
        if(x<=0.3) :
            threshMap[i][j] = 0



            
cv2.imshow("shadow",threshMap)

            
#가운데 기준으로 흰색 경계부분 검출
def fill(imgx,imglast,threshMap):
    kernel = np.ones((19,19),np.uint8)
    threshMap = cv2.morphologyEx(threshMap, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow("closing",closing)
    threshMap = cv2.GaussianBlur(threshMap, (7,7), 0)            
    cv2.imshow("fill",threshMap)
    for i in range(row):
        for j in range(col):
            if (threshMap[i][j]==0) :
                imgx[i][j]=0
                imglast[i][j]=0
    return imglast,threshMap

imglast,threshMap = fill(imgx,imglast,threshMap)

#------------------------------------------------------------------------------------------------------------------------------

image,contours, hierarchy = cv2.findContours(threshMap * 1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea)
#        image = cv2.drawContours(imgx, contours, -1, (0,255,255), 3)
#        cv2.imshow("1",image)
#for i in range(-1,2): 
#    x,y,w,h = cv2.boundingRect(contours[i])
#    if x<(col/2) and (x+w)>(col/2) and y<(row/2) and (y+h)>(row/2): #사진이 중앙에 있을 경우만 가능 - 위아래,좌우,대각선X
#        break;
#    print(i)


x,y,w,h = cv2.boundingRect(contours[-1])
aaa = threshMap[y:y+h,x:x+w]
bbb = imglast[y:y+h,x:x+w]
cv2.imshow("2",aaa)
cv2.imshow("3",bbb)



    


#cv2.imwrite("C:/Download/aaa10.jpg", bbb);





cv2.waitKey(0)
cv2.destroyAllWindows()

