import numpy as np
import math
import cv2

def getFilter(option):
    if option == "Gaussian":
        myFilter = np.zeros(shape = (3, 3), dtype = float)
        for i in range(myFilter.shape[0]):
            for j in range(myFilter.shape[1]):
                myFilter[i, j] = (math.exp(-((i - 1)**2 + (j - 1)**2)))
        myFilter = myFilter / myFilter.sum()
    elif option == "Sobel X":
        myFilter = np.float32([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    elif option == "Sobel Y":
        myFilter = np.float32([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    return myFilter

def Conv(img, option):
    myFilter = getFilter(option)
    blur = np.zeros(shape = img.shape[:2], dtype = float)
    if img.shape[-1] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Scale", img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i == 0 or j == 0 or i == img.shape[0] - 1 or j == img.shape[1] - 1:
                blur[i, j] = img[i, j]
                continue
            blur[i, j] += myFilter[0, 0] * img[i - 1, j - 1]
            blur[i, j] += myFilter[0, 1] * img[i - 1, j]
            blur[i, j] += myFilter[0, 2] * img[i - 1, j + 1]
            blur[i, j] += myFilter[1, 0] * img[i, j - 1]
            blur[i, j] += myFilter[1, 1] * img[i, j]
            blur[i, j] += myFilter[1, 2] * img[i, j + 1]
            blur[i, j] += myFilter[2, 0] * img[i + 1, j - 1]
            blur[i, j] += myFilter[2, 1] * img[i + 1, j]
            blur[i, j] += myFilter[2, 2] * img[i + 1, j + 1]
    blur = np.absolute(blur)
    return blur.astype(np.uint8)





if __name__ == "__main__":
    import cv2
    img = cv2.imread("Q2_Image/Lenna_whiteNoise.jpg")
    cv2.imshow("before", img)
    # print(img.shape, type(img))
    # cv2.imshow("after", myGaussian(img = img))