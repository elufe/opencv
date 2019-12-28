
# coding: utf-8

# In[44]:


import numpy as np
import cv2 as cv

#음식 사진에서 가장 큰 원 추출
def test(shape_img, name):
    #이미지 불러온뒤 224*224로 resize
#    shape_img = cv.resize(shape_img,(112,112),interpolation = cv.INTER_LINEAR_EXACT)

    
    #이미지 불러온뒤 gray 스케일로 변경 및 resize
    img_gray = cv.cvtColor(shape_img,cv.COLOR_BGR2GRAY)#cv.imread(name, cv.IMREAD_GRAYSCALE)
    img_gray = cv.resize(img_gray,(112,112),interpolation = cv.INTER_LINEAR_EXACT)

    img_gray = cv.medianBlur(img_gray,5)
    img_color = cv.cvtColor(img_gray,cv.COLOR_GRAY2BGR)

    #이미지에서 원을 찾는 함수
    circles = cv.HoughCircles(img_gray,cv.HOUGH_GRADIENT,1,20,
                                param1=50,param2=35,minRadius=28,maxRadius=56)
    
    #원들의 정보를 리스트로 저장
    circles = np.uint16(np.around(circles))
    
    
    y=0
    x=0
    radius = 0

    #    반지름이 가장 큰 원을 찾는 반복문
    
    for c in circles[0,:]:
        if radius < c[2] :
            
            #원의 중심 좌표
            x = c[1]
            y = c[0]
            #원의 반지름
            radius = c[2]
        

    shape_img = shape_img[x-radius : x+radius , y-radius : y+radius]
    shape_img = cv.resize(shape_img,(112,112),interpolation = cv.INTER_LINEAR_EXACT)
    

    # 자른 이미지 저장
    path = 'C:/Users/jhkim/OneDrive/Desktop/cut_img/noodle/ramen/Img_050_0' + name
    cv.imwrite(path, shape_img)

    
shape_dir = 'C:/Users/jhkim/OneDrive/Desktop/img/noodle/ramen/Img_050_0'    #사진의 절대경로

#1~1000
for idx in range(0,1100): # range(사진 시작번호 , 사진 끝번호)
    if idx < 10 :
        file_name = '00'+str(idx)+'.jpg'
    elif idx < 100 :
        file_name = '0'+str(idx)+'.jpg'
    else:
        file_name = str(idx)+'.jpg'
        
#     file_name = str(idx)+'.jpg'
   
    shape_img = cv.imread(shape_dir+file_name)
#     cv.imshow("aa",shape_img)
    try:
         test(shape_img, file_name)
    except:
         print(idx)
#     test(shape_img, file_name)

    input_key = cv.waitKey(0)
    cv.destroyAllWindows()

