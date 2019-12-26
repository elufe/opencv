
# coding: utf-8

# In[21]:


import numpy as np
import cv2 as cv


def test(shape_img, name, num):
    shape_img = cv.resize(shape_img,(224,224),interpolation = cv.INTER_LINEAR_EXACT)
    img_gray = cv.imread(name, cv.IMREAD_GRAYSCALE)
    img_gray = cv.resize(img_gray,(224,224),interpolation = cv.INTER_LINEAR_EXACT)

    img_gray = cv.medianBlur(img_gray,5)
    img_color = cv.cvtColor(img_gray,cv.COLOR_GRAY2BGR)

    circles = cv.HoughCircles(img_gray,cv.HOUGH_GRADIENT,1,20,
                                param1=50,param2=35,minRadius=60,maxRadius=112)
    circles = np.uint16(np.around(circles))
#    print(len(circles[0]))
#     for c in circles[0,:]:

#         center = (c[0],c[1])
#         radius = c[2]

#         # 바깥원
#         cv.circle(img_color,center,radius,(0,255,0),2)

#         # 중심원
#         cv.circle(img_color,center,2,(0,0,255),3)
    c = circles[0,len(circles)-1]

    center = (c[0],c[1])
    radius = c[2]

        # 바깥원
    cv.circle(img_color,center,radius,(0,255,0),2)

        # 중심원
    cv.circle(img_color,center,2,(0,0,255),3)
    
    for i in range(224):
        for j in range(224):
            if (c[0] - i)*(c[0] - i) + (c[1] - j)*(c[1] - j) > c[2]*c[2] :
                shape_img[j][i] = 0
    
#    cv.imshow("detected circles",img_color)
#    input_key = cv.waitKey(0)
#    cv.imshow("img",shape_img)
    
    path = 'C:/Users/jhkim/OneDrive/Desktop/dc/' + str(num)+'.jpg'
    cv.imwrite(path, shape_img)

#    cv.waitKey(0)
#    cv.destroyAllWindows()


shape_dir = 'C:/Users/jhkim/OneDrive/Desktop/d/Img_122_0'    #사진의 절대경로

#32000~35468
for idx in range(1,1000): # range(사진 시작번호 , 사진 끝번호)
    if idx < 10 :
        file_name = '00'+str(idx)+'.jpg'
    elif idx < 100 :
        file_name = '0'+str(idx)+'.jpg'
    else:
        file_name = str(idx)+'.jpg'
   
    shape_img = cv.imread(shape_dir+file_name)
    try:
        test(shape_img, shape_dir+file_name, idx)
    except:
        print(1)
    input_key = cv.waitKey(0)
    cv.destroyAllWindows()


# In[ ]:




