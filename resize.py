import os
import cv2
import sys
import glob
import math
# global vars to inform user whether any of his pictures were not processed well
# don't thank me, I've been through hardship of annoting whole bunch of data then augment to find myself
# with rotten missing dataset...


images= glob.glob("D:\\EVA\\EVA_S14\\bckgrd\\*")

target='D:\\EVA\\EVA_S14\\bck_rsz_new\\'

for path_to_file in images:
	scaleFactor = 0.999
	print(path_to_file)
	img = cv2.imread(path_to_file)
	print(len(img[1]),len(img[0]))
	# 1300 and 800 are arbitrary size that fits in a full screen gui
	x,y = len(img[1]),len(img[0])
	while x > 224 or y > 224: x,y = x*scaleFactor,y*scaleFactor
	x=math.ceil(x)
	y=math.ceil(y)
	print(x,y)
	resized = cv2.resize(img,(x,y),interpolation = cv2.INTER_AREA)
	filename = path_to_file.split('bckgrd\\')[1]
	print(filename)
	cv2.imwrite(target+filename,resized)

	print("Resize done",target+filename)
