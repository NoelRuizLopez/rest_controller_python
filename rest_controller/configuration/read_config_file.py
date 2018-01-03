'''
Created on 1 de dic. de 2016

@author: Noel Ruiz.Altran
'''
import os
from config import Config
import traceback
import sys

def get_config():
    _CONFIG_FILE_NAME = 'rest.conf'
    _CONFIG_RELATIVE_PATH = './'

    try:
#        cfg_file_name = os.path.splitext(cfg_file)[0] + _CONFIG_EXTENSION
        cfg_file_full_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), _CONFIG_RELATIVE_PATH, _CONFIG_FILE_NAME)
        with open(cfg_file_full_path) as the_file:
            return Config(the_file)
    except:
        traceback.print_exc()
        sys.exit(2)


