import os
import cv2
import sys
import glob
import random
import numpy as np

# function to overlay a transparent image on backround.
def transparentOverlay(src , overlay , pos=(0,0)):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    #overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    y,x = pos[0],pos[1]    # Position of PngImage
    
    #loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) # read the alpha channel 
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src



# function to overlay a transparent image on backround.
def transparentOverlay_mask(src , overlay , pos=(0,0)):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    #overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    y,x = pos[0],pos[1]    # Position of PngImage
    
    #loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) # read the alpha channel 
            src[x+i][y+j] = alpha*overlay[i][j][:4]+(1-alpha)*src[x+i][y+j]
    return src


""" ----------- Read all images --------------------"""

#root="D:\\EVA\\S14\\overlay_160"
images_bg= glob.glob("D:\\EVA\\EVA_S14\\bck_rsz_224\\*")

images_fg= glob.glob("D:\\EVA\\EVA_S14\\for_transparent\\*")

target='D:\\EVA\\EVA_S14\\overlay\\'

maskpath='D:\\EVA\\EVA_S14\\overlay_mask\\'

images_bg_sub=images_bg[0:2]
images_fg_sub=images_fg[0:2]

for bg in images_bg_sub:
	for fg in images_fg_sub:			
		for i in range(20):
			#reading background image
			src = cv2.imread(bg,cv2.IMREAD_UNCHANGED)
			h1,w1,_=src.shape
			filename = bg.split('bck_rsz_224\\')[1]
			file = filename.split('.jpg')[0]
			
			#reading overlay image
			overlay = cv2.imread(fg,cv2.IMREAD_UNCHANGED)
			h2,w2,_=overlay.shape
			filenam = fg.split('for_transparent\\')[1]
			fil = filenam.split('.png')[0]
			
			#initializing random numbers for position to place overlay image
			m=random.randint(1,(h1-h2))
			print(h1,h2,m)
			n=random.randint(1,(w1-w2))
			print(w1,w2,n)
			
			#Overlaying bg and fg
			result = transparentOverlay(src,overlay,(m,n))
			
			cv2.imwrite(target+file+"_"+fil+"_"+str(i+1)+".jpg", result)
			
			#rc=result[:,:,0]
			
			#cv2.imwrite(root+"\\"+file+"_"+fil+"_"+str(i+1)+".png", rc)
			
			#bc=result[:,:,1]
			
			#cv2.imwrite(root+"B_channel\\"+file+"_"+fil+"_"+str(i+1)+".png", bc)
			
			#gc=result[:,:,2]
			
			#cv2.imwrite(root+"G_channel\\"+file+"_"+fil+"_"+str(i+1)+".png", gc)
			
			#Creating mask
			img_RGBA =np.zeros((224,224,4), np.uint8)
			
			mask = transparentOverlay_mask(img_RGBA,overlay,(m,n))
			
			alpha_mask=mask[:,:,3]
			
			
			cv2.imwrite(maskpath+file+"_"+fil+"_"+str(i+1)+".jpg", alpha_mask)
			
			del result,src,overlay
	print("Generated images for",file)
	
	






