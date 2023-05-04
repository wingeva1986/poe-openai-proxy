import toml
import requests
import os

file="config.toml"
mytoml=toml.load(file)
list=requests.get(os.getenv('ACCPOOL_BASE_URL')+'/LIST').json()['list']
mytoml['tokens']=list
with open(file, 'w') as f:
  toml.dump(mytoml,f)
