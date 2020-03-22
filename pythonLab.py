# -*- coding: utf-8 -*-
import shutil
import os
from six.moves import input

baseDirectory = "/home/damianossotirakis/__Wiki/GitHub/Dansotirakis/PythonLab/"
destino = baseDirectory + "fileDirectory2/"
origem = baseDirectory + "fileDirectory1/"
file = "testeCopy.txt"
param1 = "teste escrevendo linha"

############[Define a função para escrever linha]################
#################################################################
def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
            file_object.write(text_to_append)


#########[Define a função para escrever varias linha]############
#################################################################
def append_multiple_lines(file_name, lines_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        # Iterate over each string in the list
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)


#######[Define a função para escrever linha especifica]##########
#################################################################
def append_specific_line(file_name, lines_to_append, param):
    with open(file_name, "r+") as f:  # r+ does the work of rw
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(param):
                lines[i] = lines[i].strip() + "\n" + lines_to_append
        f.seek(0)
        for line in lines:
            f.write(line)


#####################[Copia arquivos]############################
#################################################################
# shutil.copyfile(origem + file, destino + file)


######################[Move arquivos]############################
#################################################################
# shutil.move(origem + file, destino + file)


####################[Leitura de arquivo]#########################
#################################################################
# arquivo = open(destino+file, 'r')
# for linha in arquivo:s]
#    print(linha)
# arquivo.close()


###########[Sobresecreve todo conteudo do arquivo]###############
#################################################################
# arquivo = open(destino+file, 'w')
# arquivo.write("sobres")
# arquivo.close()


##############[Sobrescreve conteudo especifico]##################
#################################################################
# with open(destino+file) as f:
#    newText = f.read().replace("Ors", "Teste")
# with open(destino+file, 'w') as fileLoop:
#    fileLoop.write(newText)


#################[Escreve entrada no arquivo]####################
#################################################################
# inputObejct = input("Entity   : ")
# append_new_line(destino + file, inputObejct)


###########[Escreve varias entrada no arquivo]###################
#################################################################
# lines = [" teste", "  teste2", "   teste3", "    teste4"]
# append_multiple_lines(destino + file, lines)


##############[Escreve entrada linha especifica]#################
#################################################################
# inputObejct = input("Entity   : ")
# append_specific_line(destino + file, inputObejct + "\n", param1)

os.mkdir("dir/dir/dir")
