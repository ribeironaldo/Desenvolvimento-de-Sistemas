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
