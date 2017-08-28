
exercicio4 = open('exercicio4.txt', 'w')

texto = "eu não sei o que estou fazendo"
print (texto)

exercicio4.close()


lerexercicio4 = open('exercicio4.txt', 'r')
ler = lerexercicio4.readline()
print ('agora eu sei o que estou fazendo')

lerexercicio4.close()
