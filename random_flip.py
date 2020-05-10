import os
import cv2
import sys
import glob
import random


images= glob.glob("D:\\EVA\\EVA_S14\\for_transparent\\*")

target='D:\\EVA\\EVA_S14\\for_transparent_flip\\'



for path_to_file in images:
	print(path_to_file)
	img = cv2.imread(path_to_file,cv2.IMREAD_UNCHANGED)
	filename = path_to_file.split('for_transparent\\')[1]
	file = filename.split('.png')[0]
	#rndm= random.randint(1,3)
	#if rndm  <2:
	#	img_flip_ud = cv2.flip(img, 0)
	#	cv2.imwrite(target+file+"_F.png", img_flip_ud)
	#elif  rndm >2:
	img_flip_lr = cv2.flip(img, 1)
	cv2.imwrite(target+file+"_F.png", img_flip_lr)

	#else:
	#	img_flip_ud_lr = cv2.flip(img, -1)
	#	cv2.imwrite(target+file+"_F.png", img_flip_ud_lr)
	
print("Randomly fliped images saved")

