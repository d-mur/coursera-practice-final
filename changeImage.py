#!/usr/bin/env python3
from PIL import Image
import os


path_to_images = 'supplier-data/images/'
for file in os.listdir(path_to_images):
  if '.tiff' in file[-5:].lower():
    Image.open(path_to_images+file).convert('RGB').resize((600,400)).save(f'{path_to_images}{file[:-5]}.jpeg', 'JPEG')

