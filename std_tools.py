# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:23:22 2019

@author: cidm
"""
import re
import unicodedata
import datetime as dt
import pandas as pd
import numpy as np

def strip_accents(text):
    """
    Compatible with python 2.x and 3.x
    Strip accents from input string.

    :param text: The input string.
    :type text: string.

    :returns: processed string.
    :rtype: string.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def text_to_id(text, num=True):
    """
   Convert input text to id.

    :param text: The input string.
    :param num: if True removes the numbers. If false leave inside the name numbers and removes trailing character.
     num=False is ideal to remove trailing numbers only.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(str(text).lower())
    text = re.sub('[ ]+', '_', text)
    if num:
        text = re.sub('[^0-9a-zA-Z_-]', '', text)
    else:
        text = re.sub('[^a-zA-Z_-]', '', text)
        text = text[:-1]
    return text
