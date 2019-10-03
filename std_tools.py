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

def insert_cnpj(num):
    
    """
    Cast a string of digits to the formatted 00.000.000/0001-00 CNPJ standard.
    """
    cnpj = num[:2]+'.'+num[2:5]+'.'+num[5:8]+r'/'+num[8:12]+'-'+num[13:]
    return cnpj

def make_cnpj(series):
    
    """
    Force the CNPJ 00.000.000/0001-00 standard on a pandas series object.
    """
    series = series.apply(lambda x: str(x))
    series = series.apply(lambda x: x.zfill(14))
    series = series.apply(lambda x: insert_cnpj(x))
    
    return series

def insert_cpf(a):
    
    """
    Cast a string of digits to the formatted 000.000.000-00 CPF standard.
    """
    cpf = a[:3]+'.'+a[3:6]+'.'+a[6:9]+'-'+a[9:]
    return cpf

def make_cpf(series):
    
    """
    Force the CPF 000.000.000-00 standard on a pandas series object.
    """
    series = series.apply(lambda x: str(x))
    series = series.apply(lambda x: x.zfill(11))
    series = series.apply(lambda x: insert_cpf(x))
    
    return series