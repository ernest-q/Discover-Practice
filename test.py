import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt

def facialDetection():
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Ernest\\Desktop\\GitRepos\\Discover-Practice\\haarcascade_frontalface_default.xml')

    img = cv2.imread('F:\\train_sample_videos\\data\\1.jpg')

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for(x,y,w,h) in faces:
        c = math.hypot(h,w)
        print(c)
        scale = int((((-4*w)-(4*h)+math.sqrt((-16*h**2) + (32*h*w) + (72*c**2)-(16*w**2)))/16))
        print(scale)
        cv2.rectangle(img, (x-scale,y-scale), (x+w+scale,y+h+scale), (255,0,0), 2)
        print(x,y)
        print(x+w,y+h)
        print(scale)


        cv2.imshow('img',img)
        cv2.waitKey()

def vidFrame():
    cam = cv2.VideoCapture('F:\\train_sample_videos\\aagfhgtpmv.mp4')

    try:
        if not os.path.exists('F:\\train_sample_videos\\data'):
            os.makedirs('F:\\train_sample_videos\\data')

    except OSError:
        print ('Error: Creating directory of data failed')

    currentFrame = 0

    """while True:"""
    while currentFrame != 20:
        ret, frame = cam.read()

        if ret:
            name = 'F:\\train_sample_videos\\data\\' + str(currentFrame) + '.jpg'
            print('Creating...' + name)

            cv2.imwrite(name,frame)

            currentFrame += 1

        else:
            break

    cam.release()
    cv2.destroyAllWindows()

def spectrumAnalysis():
    img = cv2.imread('F:\\train_sample_videos\\data\\1.jpg',0)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    rows, cols = img.shape
    crow,ccol = rows/2 , cols/2
    fshift[int(crow-30):int(crow+30), int(ccol-30):int(ccol+30)] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    plt.subplot(131),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(img_back)
    plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    plt.show()

def main():
    vidFrame()
    spectrumAnalysis()
    facialDetection()

if __name__ == "__main__":
    main()