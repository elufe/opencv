
# coding: utf-8

# In[ ]:


import numpy as np
import cv2 as cv

#음식 사진에서 가장 큰 원 추출, 매개변수 -> 이미지
def test(shape_img):
    #이미지 불러온뒤 224*224로 resize
    shape_img = cv.resize(shape_img,(112,112),interpolation = cv.INTER_LINEAR_EXACT)
    
    #이미지 불러온뒤 gray 스케일로 변경 및 resize
    img_gray = cv.imread(name, cv.IMREAD_GRAYSCALE)
    img_gray = cv.resize(img_gray,(112,112),interpolation = cv.INTER_LINEAR_EXACT)

    img_gray = cv.medianBlur(img_gray,5)
    img_color = cv.cvtColor(img_gray,cv.COLOR_GRAY2BGR)

    #이미지에서 원을 찾는 함수
    circles = cv.HoughCircles(img_gray,cv.HOUGH_GRADIENT,1,20,
                                param1=50,param2=35,minRadius=20,maxRadius=56)
    
    #원들의 정보를 리스트로 저장
    circles = np.uint16(np.around(circles))
    

    #찾은 원들중에 가장 큰 원의 정보 저장
    c = circles[0,len(circles)-1]

    #원의 중심 좌표
    center = (c[0],c[1])
    
    #원의 반지름
    radius = c[2]
    print(c[0], c[1], c[2])
    # 바깥원
    cv.circle(img_color,center,radius,(0,255,0),2)

    # 중심원
    cv.circle(img_color,center,2,(0,0,255),3)
    
    # 원 밖의 이미지부분 제거
    for i in range(112):
        for j in range(112):
            if (c[0] - i)*(c[0] - i) + (c[1] - j)*(c[1] - j) > c[2]*c[2] :
                shape_img[j][i] = 0

    # 자른 이미지 저장
#     path = 'C:/Users/jhkim/OneDrive/Desktop/' + str(num+10)+'.jpg'
#     cv.imwrite(path, shape_img)

    # 자른 이미지 리턴
    return shape_img

