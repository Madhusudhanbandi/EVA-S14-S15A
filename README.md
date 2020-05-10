# EVA-S14-S15A
Creation of CUSTOM DATASET with 400k images and monocular depth estimation and segmentation
1.Link to custom dataset

1.https://drive.google.com/open?id=1A1yyMDtNm7lCtDWAmDZL1bGPinw9sLsj

Overlayed fackground and background images zip file: bgfg_images.zip
Mask images zip file: fgmask_images.zip  
Depth images file: depthimages.zip

2.Steps followed to create custom dataset
2.1.There are background, foreground, overlayed foreground on background,mask images, depthimages
2.2.100 bg, 200 fg, 400k overlayed, 400k mask, 400k depth images
2.3.Total size of datasets is 4 GB 
2.4 Summary staticstcs 
Background images - Means of RGB channels is: [139.47920022 149.2706545  156.24668327]
Background images - Std of RGB channels is: [70.37698057 67.25921999 66.53126658]

Foreground images - Means of RGBA channels is: [28.83108492 29.49019002 34.96438342 78.30303782]
Foreground images - Std of RGBA channels is: [ 53.45716788  56.41516636  65.68626786 115.27612109]

Mask images - Means of mask images is: [78.30467003]
Mask images - Std of mask images is: [115.14415228]

3.Images

4.Steps followed to create custom datasets 
4.1.Foreground images were created by removing the background using powerpoint and random flips of 100 foreground images were created(total of 200 foreground with transparent background were created)
4.2.Masks were created by taing the alpha channel from png foreground images
4.3.Iterated over all the pixels in the foreground image and extracted alphachannel and scalled and blended using blending equation to the source image and for each background image 200 foreground images at 20 random positions of the background image and masks were created for all the overlayed foreground images by extracting alpha channel.
4.4 Depth estimation was made on the custom dataset 
4.4.Depth images were created for all the overlayed images. 

