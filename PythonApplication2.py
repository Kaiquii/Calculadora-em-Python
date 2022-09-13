print ("###################################################################")
print ("######################   CALCULADORA 1.0.1 ########################")
print ("###################################################################")
print ("Digite um simbolo para fazer um determinado calculo ,+,-,*,/,raiz,sen,cos,tan...")
import math
while True:  
 Operação = input("Digite a operação:")
 if Operação == "+":
     numero1 = input("Digite um valor:")
     numero2 = input("Digite um valor:")
     Resultado = int(numero1) + int(numero2)
     print ("O resultado da operação é: " + str(Resultado)) 
 if   Operação == "-":
     numero1 = input("Digite um valor:")
     numero2 = input("Digite um valor:")
     Resultado = int(numero1) - int(numero2)
     print ("O resultado da operação é: " + str(Resultado))
 if Operação == "*":
     numero1 = input("Digite um valor:")
     numero2 = input("Digite um valor:")
     Resultado = int(numero1) * int(numero2)
     print ("O resultado da operação é: " + str(Resultado))
 if Operação == "/":
     numero1 = input("Digite um valor:")
     numero2 = input("Digite um valor:")
     Resultado = int(numero1) / int(numero2)
     print ("O resultado da operação é: " + str(Resultado))
 if Operação == "raiz":
     numero = int(input("Digite um valor:"))
     raiz = math.sqrt(numero)
     print ("O resultado da operação é: " , (raiz))
 if Operação == "sen":
     ângulo = float(input("Digite o ângulo que você deseja: "))
     seno = math.sin(math.radians(ângulo))
     print("O ângulo de {} tem o seno de {:.2f}". format(ângulo, seno))
 if Operação == "cos":
     ângulo = float(input("Digite o ângulo que você deseja: "))
     cosseno = math.cos(math.radians(ângulo))
     print("O ângulo de {} tem o cosseno de {:.2f}". format(ângulo, cosseno))
 if Operação == "tan":
     ângulo = float(input("Digite o ângulo que você deseja: "))
     tangente = math.tan(math.radians(ângulo))
     print("O ângulo de {} tem o tangente de {:.2f}". format(ângulo, tangente))
 if Operação == "sair":
     break

     

    
    
      

     



 
 