from logging import exception
original_sentence = "This is a common interview question"

# find the most repeated letter in the question

sentence_list = []

for letter in original_sentence:
    #   #print(letter)
    sentence_list.append(letter)
#     #letter_to_compare = letter[letter]
#     # print(letter_to_compare)
#     #
print(sentence_list)

# z = 0
# for x in enumerate(sentence_list):
#     new_indice = x[0]
#     letter_to_test = x[1]
#     for y in enumerate(sentence_list):
#         letter_to_compare = x[1]
#         if letter_to_compare == letter_to_test:
#             z = z + 1


# # 23 - Exercise

# sentence = "This is a common interview question"

# # find the most repeated letter in the question

# sentence_list = []

# for letter in sentence:
#     #   #print(letter)
#     sentence_list.append(letter)
# #     #letter_to_compare = letter[letter]
# #     # print(letter_to_compare)
# #     #
# #     #
# z = 0
# for x in enumerate(sentence_list):
#     new_indice = x[0]
#     letter_to_test = x[1]
#     for y in enumerate(sentence_list):
#         letter_to_compare = x[1]
#         if letter_to_compare == letter_to_test:
#             z = z + 1
#     k = z


# #


try:
    file = open("app.py")
    age = int(input("Enter your age: "))
    xfactor = age/0
except (ValueError, ZeroDivisionError):
    print("You didn't entered a value age. ")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
print("Execution continues.")
