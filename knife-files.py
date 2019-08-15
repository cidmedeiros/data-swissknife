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
        
def folha_rosto_proeb(data):
    for index, bolsista in data.iterrows():
        entidade = bolsista.nome_entidade_local
        f_dir = re.sub('/', '_', entidade)
        f_dir = f_dir.upper()
        n_sei = ''
        n_cpf = bolsista.cpf_bolsista
        b_nome = bolsista.nome_bolsista
        if not os.path.exists(f_dir):
            os.makedirs(f_dir)
        template = 'folha-rosto.docx'
        document = mg.MailMerge(template)
        document.merge(ies=entidade, sei=n_sei, cpf=n_cpf, nome=b_nome)
        document.write('{}/{}.docx'.format(f_dir,bolsista.nome_bolsista))

def lista_ies_proeb(data):
    ies_list = list(data.nome_entidade_local.unique())
    for ies in ies_list:
        os.chdir(r'C:\Users\cidm\Documents\python_control\proeb')
        f_dir = re.sub('/', '_', ies)
        f_dir = f_dir.upper()
        if not os.path.exists(f_dir):
            os.makedirs(f_dir)
        os.chdir(r'{}'.format(f_dir))
        bolsistas_list = data.query('nome_entidade_local == "{}"'.format(ies))
        if len(ies)> 30:
            nome_ies = ies[:31]
            nome_ies = re.sub('/', '_', nome_ies)
        else:
            nome_ies = re.sub('/', '_', ies)
        excel(bolsistas_list, nome_ies)


