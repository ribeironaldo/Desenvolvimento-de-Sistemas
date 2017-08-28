#1
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
