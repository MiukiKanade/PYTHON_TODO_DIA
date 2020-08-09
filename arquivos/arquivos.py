#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

#path é o caminho onde os arquivos estão (imagens, ou qualquer outra coisa)
path = 'C:\\Users\\miuki\\Documents\\LAB\\SOLON\\E3\\pos\\'
#cria arquivo para escrita e atualização
arquivo = open('nomes_imagens.txt', 'a')

for caminho, d, file in os.walk(path):
    for filename in file:
        #filename é o nome dos arquivos dentro de path
        arquivo.write(filename+'\n')

#fecha arquivo IMPORTANTE!!!
arquivo.close()

