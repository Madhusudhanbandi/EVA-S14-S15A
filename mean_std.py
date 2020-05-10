import os
import cv2
import sys
import glob
import random
import numpy as np

target=glob.glob('D:\\EVA\\s14\\overlay_bg_fg\\*')
		
pixel_mean = np.zeros(3)
pixel_std = np.zeros(3)
k = 1
for image in target:
	img = cv2.imread(image,cv2.IMREAD_UNCHANGED)
	pixels = img.reshape((-1, img.shape[2]))
	for pixel in pixels:
		diff = pixel - pixel_mean
		pixel_mean += diff / k
		pixel_std += diff * (pixel - pixel_mean)
		k += 1
pixel_std = np.sqrt(pixel_std / (k - 2))
print("Means of RGB channels is:",pixel_mean)
print("Std of RGB channels is:",pixel_std)
