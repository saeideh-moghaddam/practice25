from typing import *
import cv2
import numpy as np 

image = cv2.imread("sol.jpg", 0)
def convolution(image , dimension):
    image = cv2.imread("sol.jpg", 0)
    mask = np.ones((dimension , dimension)) / (dimension **2)
    result = np.zeros(image.shape)
    rows , cols = image.shape

    for i in range(dimension //2 ,rows-(dimension //2)):
        for j in range(dimension//2 ,cols-(dimension // 2 )):
            small_img = image[i-(dimension//2):i+1+(dimension//2) ,j-(dimension//2):j+1+(dimension//2)]
            result[i ,j] = np.sum(small_img * mask)

    cv2.imwrite("melody.jpg" , result)


print("""enter the dimension image\t3. 3*3\t5. 5*5\t7. 7*7\t15. 15*15""")
option = int(input())
convolution(image, option)