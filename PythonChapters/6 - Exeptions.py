6 - EXEPTIONS

== == == == == == == == == == == == == == == = 2 - Handling Exeptions == == == == == == == == == == == == == == == =


# try:
#     print()
#     file = open("app.py")
#     age = int(input("Enter your age, "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You entered a wrong age: ")
# else:
#     print("No exeption to thrown. ")
# finally:
#     file.close()
# print()
# # print("xfactor: ", xfactor)
# print()


# Raising Exeptions

def calculate_xfactor(age):
    if age < 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


print(calculate_xfactor(10))
