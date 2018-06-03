from skimage import io
import matplotlib.pyplot as plt
import math
def distance(color1, color2):
    dif = 0
    for i in range(0,3):
        dif = dif + math.pow((color1[i]-color2[i]),2)
    return math.sqrt(dif)

def removeRedEye(image,startX,endX,startY,endY,red_eye):
    rows,cols,dims=image.shape
    for i in range(0,rows):
        for j in range(0,cols):
            if (startX <= i <= endX) and (startY <= j <= endY):
                if distance(red_eye,image[i,j])<150:
                    image[i,j,0] = 50
                    image[i,j,1] = 50
                    image[i,j,2] = 50
    return image
img=io.imread('red_eye2.jpg')
io.imshow(img)
red_eye = [250, 20, 20]
img2 = removeRedEye(img, 70, 100, 50, 220, red_eye)
plt.figure()
io.imshow(img2)
io.show()