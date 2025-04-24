# Segemntation Filters Project
# Done By Amr Badran (12113636)
# DeadLine : 26/12/2023 11:59 PM
# Last Modification : 24/12/2023 8:20 PM

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
class filters:

    def __init__(self,img):
        self.img = img
    
    def thershold(self , T):
        # _ , thresh --> _ mean that i dont care about the first return value in python
        _ ,thresh  = cv.threshold(self.img,T,255,cv.THRESH_BINARY)
        return thresh
    def inversethreshold(self , T):
        # _ , thresh --> _ mean that i dont care about the first return value in python
        _ ,thresh  = cv.threshold(self.img,T,255,cv.THRESH_BINARY_INV)
        return thresh
    def pointDetect(self):
        # set the 2d Array (filter 2d)
        array = [
            [-1,-1,-1],
            [-1,8,-1],
            [-1,-1,-1]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def horizntalLine(self):
        # set the 2d Array (filter 2d)
        array = [
            [-1,-1,-1],
            [2,2,2],
            [-1,-1,-1]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def verticalLine(self):
         # set the 2d Array (filter 2d)
        array = [
            [-1,2,-1],
            [-1,2,-1],
            [-1,2,-1]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def F45Line(self):
        # set the 2d Array (filter 2d)
        array = [
            [-1,-1,2],
            [-1,2,-1],
            [2,-1,-1]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def FN45Line(self):
        # set the 2d Array (filter 2d)
        array = [
            [2,-1,-1],
            [-1,2,-1],
            [-1,-1,2]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def horizntalEdge(self):
        # set the 2d Array (filter 2d)
        array = [
            [-1,-2,-1],
            [0,0,0],
            [1,2,1]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def verticalEdge(self):
        # set the 2d Array (filter 2d)
        array = [
            [-1,0,1],
            [-2,0,2],
            [-1,0,1]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def F45Edge(self):
        # set the 2d Array (filter 2d)
        array = [
            [-2,-1,0],
            [-1,0,1],
            [0,1,2]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def FN45Edge(self):
        # set the 2d Array (filter 2d)
        array = [
            [0,1,2],
            [-1,0,1],
            [-2,-1,0]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def Laplacian(self):
        # set the 2d Array (filter 2d)
        array = [
            [0,-1,0],
            [-1,4,-1],
            [0,-1,0]
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def LOG(self):
        # set the 2d Array (filter 2d)
        array = [
            [0,0,-1,0,0],
            [0,-1,-2,-1,0],
            [-1,-2,16,-2,-1],
            [0,-1,-2,-1,0],
            [0,0,-1,0,0],
        ]
        #array = 2 * array
        kernal = np.array(array) #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal) # apply the filter
        return img
    def customFilter(self,custom_array):
        array = custom_array # receive the 2d filter
        #array = 2 * array
        kernal = np.array(array)  #set the kernal using numpy 
        img = cv.filter2D(self.img,-1,kernal)# apply the filter
        return img
       
    

# this will excute only if we run filters.py independetly (not called by another class)
if __name__ == "__main__":
    image_input_path = "images/tmp.PNG"
    img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
    cv.imshow('Image Before',img) 
    obj = filters(img)
    matrix = np.full((15, 15), 1/225)
    img2 = obj.customFilter(matrix)
    cv.imshow('Image After',img2) 
    cv.waitKey(0)