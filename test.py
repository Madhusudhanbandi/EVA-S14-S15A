import os
import glob
import argparse
import matplotlib
from zipfile import ZipFile
import zipfile
from PIL import Image

# Keras / TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model
from layers import BilinearUpSampling2D
from utils import predict, load_images, display_images,to_multichannel
from matplotlib import pyplot as plt

# Argument Parser
parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
parser.add_argument('--model', default='nyu.h5', type=str, help='Trained Keras model file.')
parser.add_argument('--input', default='/content/gdrive/My Drive/Colab Notebooks/S14/DenseDepth/bgfg_images.zip', type=str, help='Input filename or folder.')
parser.add_argument('--st', default=0, type=int)
parser.add_argument('--sp', default=1000, type=int)
parser.add_argument('--bs', default=10, type=int)
args = parser.parse_args()

# Custom object needed for inference and training
custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}

print('Loading model...')

# Load model into GPU / CPU
model = load_model(args.model, custom_objects=custom_objects, compile=False)

print('\nModel loaded ({0}).'.format(args.model))

# Input images
inputs = load_images( args.input, args.st,args.sp )
print('\nLoaded ({0}) images of size {1}.'.format(inputs.shape[0], inputs.shape[1:]))
# Compute results
outputs = predict(model, inputs,batch_size=args.bs)

import zipfile
out_zip = zipfile.ZipFile('depthimages.zip', mode='a', compression=zipfile.ZIP_STORED)

from pathlib import Path

Path(f'depth/').mkdir(parents=True, exist_ok=True)


i=0
with ZipFile(args.input, 'r') as zip:
    image_files=zip.namelist()
    for image in image_files[args.st:args.sp]:
        out_zip = zipfile.ZipFile('depthimages.zip', mode='a', compression=zipfile.ZIP_STORED)
        filename = image.split('/')[-1]
        file = filename.split('.jpg')[0]
        output=to_multichannel(outputs[i])
        imd = Image.fromarray(output[:,:,0]*255)
        imd= imd.convert('L')
        imd.save('d_temp.jpg')
        out_zip.write('d_temp.jpg', f'depth/{file+"_D"+".jpg"}')
        out_zip.close()
        i +=1
        del output, imd
    del outputs
print(i)
    

