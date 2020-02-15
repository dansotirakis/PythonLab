import shutil

destino = '/home/damianossotirakis/PycharmProjects/autoBoots/fileDirectory1/'
origem = '/home/damianossotirakis/PycharmProjects/autoBoots/fileDirectory2/'
file = 'testeCopy.txt'


#shutil.copyfile(origem + file, destino + file)
#shutil.move(origem + file, destino + file)

##Modo escrita
#arquivo = open(destino+file, 'w')

##Sobresecreve conteudo do arquivo
#arquivo.write("sobres")
#arquivo.close()

##Leitura linha linha
#arquivo = open(destino+file, 'r')
# for linha in arquivo:s]
#    print(linha)
#arquivo.close()

##Sobrescreve conteudo especifico
with open(destino+file) as f:
    newText = f.read().replace("Ors", "Teste")

with open(destino+file, 'w') as fileLoop:
        fileLoop.write(newText)

arquivo = open(destino+file, 'r')
for linha in arquivo:
    print(linha)
arquivo.close()
