import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('siqijor_noise_1.jpg', 0)                                          #Reads the original image

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)                       #Defines the image as float32, defines the Fourier Transform; Complex output contains both the complex and imaginary values, so the element has three dimensions (will be important later)
dft_shift = np.fft.fftshift(dft)                                                    #Defines the 'shift'

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))   #Defines the magnitude spectrum; Uses logarithm for better representation on graph ('narrows' max and min values)

cv2.imwrite('siqijor_magnitude_1.jpg', magnitude_spectrum)                            #Saves the magnitude spectrum image as a file (needed for Photoshop to create image mask)

img_mask = cv2.imread('noise_mask_1.bmp', 0)                                        #Reads the mask image (generated in Photoshop)
img_mask_min = np.amin(img_mask)                                                    #Finds the minimum value of image (should be 0)
img_mask_max = np.amax(img_mask)                                                    #Finds the maximum value of image (should be 255)

img_mask_normalized = img_mask / 255                                                #Normalizes the image (the idea is to narrow all the values between 0 and 1)
img_mask_normalized_min = np.amin(img_mask_normalized)                              #Finds the minimum value of image (should be 0)
img_mask_normalized_max = np.amax(img_mask_normalized)                              #Finds the minimum value of image (should be 1)

img_mask_full = np.float32(np.dstack((img_mask_normalized, img_mask_normalized)))   #Stacks the image mask into three dimensions (in order to be able to broadcast with dft_shift) and creates a float

fshift = dft_shift * img_mask_full                                                  #This is where the magic happens - by using the image mask, we are 'blocking' certain frequencies (black areas of mask)
f_ishift = np.fft.ifftshift(fshift)                                     

img_back = cv2.idft(f_ishift)                                                       #Applies the shift to the return image
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])                           #Creates the final return image from magnitude spectrum

plt.subplot(221),plt.imshow(img, cmap = 'gray')                                     #Creates plot of original image
plt.title('Input Img'), plt.xticks([]), plt.yticks([])
                          
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')                      #Creates plot of magnitude spectrum image
plt.title('Mag. Spect.'), plt.xticks([]), plt.yticks([])  

plt.subplot(223),plt.imshow(img_mask, cmap = 'gray')                                #Creates plot of image mask
plt.title('Mask'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(img_back, cmap = 'gray')                                #Creates plot of return image
plt.title('Return Image'), plt.xticks([]), plt.yticks([])
plt.show()