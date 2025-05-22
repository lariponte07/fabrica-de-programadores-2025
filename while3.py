#n= int(input("Tabuada de: "))
#x=1
#while x <=10:
    #print(n+x)
    #x=x+1

#n = int(input("Tabuada de: "))
#x=1
#while x <=10:
    #print(n*x)
    #x=x+1

#ex1

#n = int(input("Tabuada de: "))
#x=1
#while x <=10:
    #print(n,"x",x,"=",n*x)
    #x=x+1

#ex2
#n1 = int(input("Digite o primeiro número da tabuada:"))
#n2 = int(input("Digite o último número da tabuada: "))

#x=1
#while x <= n2:
    #print(n1,"x",x,"=",n1*x)
    #x=x+1

#s=0
#while True:
    #v=int(input("Digite um número : "))
    #if v==0:
        #break
    #s=s+v
#print(s)

lista =[]
soma = 0
while True:
    numero =int(input("Digite um número inteiro:"))
    if numero == 0:
        break
    soma += numero
    lista.append(numero)
print("o resultado da soma é:",soma)
print("A média aritmética é: ",soma/len(lista))


