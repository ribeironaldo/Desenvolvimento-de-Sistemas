#Exercicio 1

def ex1(vet):
    for i in range(3):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet
 
vet = [0]*3
for i in range(3):
    vet[i] = int(input('Digite um valor: '))
print(vet)
ex1(vet)
print(vet)

----------------------------------------------------------

#Exercicio 2

def ex2(vet, tam):
    for i in range(tam):
        if vet[i] < 0:
            vet[i] = 0
        elif vet[i] < 10:
            vet[i] = 1
        else:
            vet[i] = 2
    return vet
 
tam = 3
 
vetor = [0]*tam
for i in range(tam):
    vetor[i] = int(input('Digite um valor: '))
ex2(vetor,tam)
print(vetor)

----------------------------------------------------------

#Exercicio 3

valor = int(input("digite um valor : "))

if valor < 0:
    print (valor*-1)
elif valor > 10:
    valor2 = int(input("digite segundo valor de referência: "))
    print (valor - valor2)
else:
    print (valor/5)


----------------------------------------------------------

#Exercicio 4

exercicio4 = open('exercicio4.txt', 'w')

texto = "eu não sei o que estou fazendo"
print (texto)

exercicio4.close()


lerexercicio4 = open('exercicio4.txt', 'r')
ler = lerexercicio4.readline()
print ('agora eu sei o que estou fazendo')

lerexercicio4.close()


----------------------------------------------------------

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


