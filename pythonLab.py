import shutil

baseDirectory = '/home/damianossotirakis/__Wiki/GitHub/Dansotirakis/PythonLab/'
destino = baseDirectory+'fileDirectory2/'
origem = baseDirectory+'fileDirectory1/'
file = 'testeCopy.txt'


######################[Copia arquivos]###########################
#################################################################
#shutil.copyfile(origem + file, destino + file)


######################[Move arquivos]############################
#################################################################
#shutil.move(origem + file, destino + file)


####################[Leitura de arquivo]#########################
#################################################################
#arquivo = open(destino+file, 'r')
# for linha in arquivo:s]
#    print(linha)
#arquivo.close()


###############[Sobresecreve conteudo do arquivo]################
#################################################################
#arquivo = open(destino+file, 'w')
#arquivo.write("sobres")
#arquivo.close()


##############[Sobrescreve conteudo especifico]##################
#################################################################
#with open(destino+file) as f:
#    newText = f.read().replace("Ors", "Teste")
#with open(destino+file, 'w') as fileLoop:
#        fileLoop.write(newText)
#arquivo = open(destino+file, 'r')
#for linha in arquivo:
#    print(linha)
#arquivo.close()

