# Criando um objeto do tipo file
relatorio = open("relatorio.txt", "w")

import math

def soma(espaco):
    return sum(espaco)

def media(espaco):
    return float(sum(espaco))/len(espaco)

# Escrevendo no arquivo

relatorio.write("ACME Inc.    Uso do espaço em disco pelos usuários\n")
relatorio.write("-"*50)
relatorio.write("\n Nr.   Usuário     Espaço Utilizado    % do Uso \n")
user = ["Alexandre" , "Anderson", "Antonio", "Carlos", "Cesar", "Rosemary"]
espaco = [434.99, 1187.99, 117.73, 87.03, 0.94, 752.88]
perc = [16.85, 46.02, 4.56, 3.37, 0.04, 29.16]

for i in range(6):
    relatorio.write('\n %i     %s       %4.2f MB      %4.2f %% \n' % (i+1 , user[i], espaco[i], perc[i]))

relatorio.write("\nEspaço total ocupado: %4.2f MB \n" %(soma(espaco)))
relatorio.write("Espaço médio ocupado: %4.2f MB \n" %(media(espaco)))

# Fechando o arquivo
relatorio.close()
