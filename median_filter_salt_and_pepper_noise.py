import random
import cv2
import numpy as np

def add_salt_and_pepper_noise(image, percent_noise):
    if(percent_noise >50):
        return -1
    global pixel_count
    
    while(True):
        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                
                mode = random.randrange(0,50)
                
                if (mode == 1):
                    #salt pixels to be added
                    image[x,y] = 255
                    pixel_count = pixel_count + 1
                    
                if (mode == 9):
                    #pepper pixels to be added
                    image[x,y] = 0
                    pixel_count = pixel_count + 1
                
                #noise_percent = float(pixel_count*100)/(image.shape[0] * image.shape[1])
                
                if pixel_count > ((image.shape[0] * image.shape[1]) * percent_noise / 100) : 
                    #print noise_percent, pixel_count
                    return image

def remove_salt_and_pepper_noise(image):
    
    for x in range(1, image.shape[0]-1):
        for y in range(1, image.shape[1]-1):
            
            #we use 3x3 window for median filter
            kernel_mat = np.zeros(9)
                
            kernel_mat[0] = image[x,y]        #centre pixel
            kernel_mat[1] = image[x-1,y]      #left
            kernel_mat[2] = image[x-1,y+1]    #bottom left
            kernel_mat[3] = image[x,y+1]      #bottom
            kernel_mat[4] = image[x+1,y+1]    #bottom right
            kernel_mat[5] = image[x+1,y]      #right
            kernel_mat[6] = image[x+1,y-1]    #top right
            kernel_mat[7] = image[x,y-1]      #top
            kernel_mat[8] = image[x-1,y-1]    #top left
                
            image[x,y] = np.median(kernel_mat)
                
    return image
                
pixel_count = 0
inp_img = cv2.imread('D:/UDEMY/Computer Vision in Python/04 Image Segmentation/04-Codes/nature.jpg')
gray_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Input-Image", inp_img)

sal_img = add_salt_and_pepper_noise(gray_img, 20)
cv2.imshow("Salt & Pepper Noise-Image", sal_img)

filter_img = remove_salt_and_pepper_noise(sal_img)
cv2.imshow("Filtered Image", filter_img)

cv2.waitKey(0)
cv2.destroyAllWindows()