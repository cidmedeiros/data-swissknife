# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:00:44 2019

@author: Corey Schafer source:https://www.youtube.com/watch?v=ve2pmm5JqmI
"""
def manual_rename_files():
    """
    Creates a stream-process for renaming all the files in a directory.
    """
    import os
    from pathlib import Path
    dir_path = input('Folder location:')
    os.chdir(Path(dir_path))
    print('Current Folder: ', os.getcwd())
    print(' ')
    print('Current files: ')
    for f in os.listdir():
        f_name, f_ext = (os.path.splitext(f))
        new_name = input('New name for file {}:'.format(f_name))
        os.rename(f, new_name)    

