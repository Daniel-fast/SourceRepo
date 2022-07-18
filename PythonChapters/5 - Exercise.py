# 23 - Exercise
# from a given sentence, compare letters and show what letter occurs more times in the sentence.

# Mosh Solution 

from pprint import pprint

frase = "Abobrinha"  #Ele não esta tratando minusculas e nem maiúsculas, nem retirando os espaços
char_frequency = {}

for char in frase: # usou soment um for loop
    if char in char_frequency: #usou uma estrutura na qual ele consiste se é verdadeiro ele automaticamente soma os valores 
        char_frequency[char] += 1 # PARECE QUE O APENDE É FEITO DESTA FORMA 
    else:
        char_frequency[char] = 1
#### MUITO INTERESSANTE *****  ELE NÃO USOU APEND PARA ADICIONAR OS REGISTROS AO DICINÁRIO

print(char_frequency)
print()



pprint(sorted(char_frequency.items(),key=lambda kv: kv[1],reverse=True), width=10)

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])

#=========================================================================================================================
#Daniel´s solution
from hashlib import new
from traceback import format_exc
from typing import Any


original_sentence = "This is a common interview question"
lower_sentence = original_sentence.lower()
transformed_sentence = lower_sentence.replace(" ", "")
word_to_work = "a"
list_to_work = []
list_copy = []
word_summary = {} #Dictonary 
sentence_list = []

for letter in transformed_sentence:
    sentence_list.append(letter)
    list_to_work.append(letter)

letras_unicas = set(list_to_work)
print()
print()
print("Sentença original:", original_sentence)
print()
print("sentence_list", sentence_list)
print()
print("letras_unicas", letras_unicas)
# print()
z = 0

for x in enumerate(letras_unicas):
    
    new_indice = x[0]
    letter_to_test = x[1]
    
    for y in enumerate(list_to_work):
        letter_tobe_compared = y[1]
        if letter_to_test == letter_tobe_compared:
            z += 1
            
    word_summary[letter_to_test] = z
    z = 0
value_key_pairs = ((value, key) for (key,value) in word_summary.items())
sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
first = sorted_value_key_pairs[0]
print()
print("O maior número de ocorrências x letras é:", first)
print()
print()
