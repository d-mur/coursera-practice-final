#! /usr/bin/env python3
import os
import requests


path_to_descr = 'supplier-data/descriptions/'
url = r'http://35.232.57.32/fruits/'
for file in sorted(os.listdir(path_to_descr)):
  if file[-4:].lower() == '.txt':
    with open(path_to_descr+file, 'r') as f:
      lines = f.readlines()
      lot = {}
      lot['name'] = lines[0].strip()
      lot['weight'] = int(lines[1].split()[0])
      lot['description'] = lines[2].strip()
      lot['image_name'] = file[:-4]+'.jpeg'
      r = requests.post(url, data=lot)
      if r.status_code == 201:
        print(file+': OK')
      else:
        print(file+': '+r.reason)
