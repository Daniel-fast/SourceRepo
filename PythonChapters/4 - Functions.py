4 - FUNCTIONS 

=============================== 1 - Defining Functions   =============================== 

from pyclbr import Function
# Working with function
# Function to write a sequence of fibobacci series up to n                
def fib(n):    
a, b = 0, 1
    # a = 0
    # b = 1
while a < n:
    print(a, end='  ')
        # a, b = b, a+b
    a = b
    b = a+b
print()

# Now call the function we just defined:
fib(100)


=============================== 6 - xargs   =============================== 

# xargs
from xmlrpc.server import resolve_dotted_attribute


def matriz(*numbers):
    return numbers


def resultado(matriz):
    return matriz * 2


valores = matriz(3, 4, 6)

novo_resultado = resultado(valores)

for i in novo_resultado:
    print(i)


# Functions
# 1 - functions that perform a task
from tkinter import W


def dormir(nome_insone, hora_deitar, hora_acordar, motivo_sono):
    print(f"{nome_insone}, você deve se deitar as {hora_deitar} e acordar as {hora_acordar} porque você {motivo_sono}!")
    print()
    print("Tudo irá se resolver!!")
    print()
    print()


dormir("Pedro", "22h00", "06h00", "esta com a vida fácil")

dormir("Daniel", "23h00", "05h30", "tá fudido")

# Two types of functions
# 1 - functions that perform a task
# 2 - functions that return a value


def descansar(nome_insone, hora_deitar, hora_acordar, motivo_sono):
    return f"{nome_insone}, você deve se deitar as {hora_deitar} e acordar as {hora_acordar} porque você {motivo_sono}!"


message = descansar("Carlos", 12, 5, "tem que trabalhar")
file = open("deitar.txt", "w")
file.write(message)


def multiplicar(numero, multiplicador=2):
    return numero * multiplicador


novo_valor = 50 * multiplicar(numero=10, multiplicador=30)

print(novo_valor)






=============================== 7 - xxargs =============================== 


def dados(**informacao):
    print(informacao)


dados(nome="Daniel", valor="Alto", estuda="Muito", tipo_gostoso="Muito")











=============================== 12 - Exercise =============================== 
Exercicio fizz_buzz (Daniel)


digita_numeros = True

while digita_numeros:
    entrada = input("> ")
    if entrada.lower == "quit":
        digital_numeros = False
        break
    numero_inteiro = int(entrada)

    if numero_inteiro % 3 == 0 and numero_inteiro % 5 == 0 and numero_inteiro != 0:
        print()
        print("FizzBuzz!!!")
        print()
        print()
    else:
        if numero_inteiro % 3 == 0 and numero_inteiro != 0:
            print()
            print("Fizz")
            print()
        else:
            if numero_inteiro % 5 == 0 and numero_inteiro != 0:
                print()
                print("Buzz")
                print()
            else:
                print("> Echo:", numero_inteiro)


# Exercise Mosh
def fizz_buzz(input):
    if (input != 0) and (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"

    if (input != 0) and (input % 3 == 0):
        return "Fizz"

    if (input != 0) and (input % 5 == 0):
        return "Buzz"

    return input


print(fizz_buzz(15))                