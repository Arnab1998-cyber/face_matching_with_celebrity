import yaml
import os
import logging

def read_yaml(file):
    with open(file, 'r') as f:
        content=yaml.safe_load(f)
    return content

def create_directory(dirs:list):
    for dir in dirs:
        os.makedirs(dir,exist_ok=True)
        logging.info('directory {} is created'.format(dir))

