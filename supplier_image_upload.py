#!/usr/bin/env python3
import requests
import os


url = "http://localhost/upload/"
path_to_images = 'supplier-data/images/'
for file in os.listdir(path_to_images):
  if '.jpeg' in file[-5:].lower():
    with open(path_to_images+file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
