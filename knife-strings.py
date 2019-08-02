# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:48:56 2019

@author: cidmedeiros
"""
def strip_punct(str_list):
    import string
    no_punctuation_documents = []
    for i in str_list:
        no_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))
    return no_punctuation_documents
