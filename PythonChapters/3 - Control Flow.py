3 - CONTROL FLOW 

=============================== 2 - Conditional statments =============================== 

TEMPERATURE = 35
if TEMPERATURE > 30:
    print("It's warm")
    print("Drink water")
elif TEMPERATURE > 20:
    print("It's OK - like Guaruja right now")
else:
    print("It's cold")

print("Done")


3 - Ternary Operators
# Ternary operator

AGE = 22
if AGE > 18:
   MESSAGE = "Elegible"
else:
   MESSAGE = "Not eligible"


MESSAGE = "Eligible" if AGE > 18 else "Not eligible"
print(MESSAGE)



=============================== 4 - Logical Operators=============================== 

# Logical Operators

HIGH_INCOME = False
GOOD_CREDIT = True
STUDENT = False

# if HIGH_INCOME or GOOD_CREDIT:
#    print("Eligible")
# else:
#    print("Not eligible")

MESSAGE = "Elegivel" if (
    HIGH_INCOME and GOOD_CREDIT) and not STUDENT else "Não elegível"
print(MESSAGE)


# Chaining comparison operators

AGE = 17

if 18 <= AGE < 65:
    print("Elegível sim")
else:
    print("Sai fora")

=============================== 8 - For Loops =============================== 

for x in [1, 4, 5, 7, 3]:
    print(x)


NUMBER = 100
while NUMBER > 0:
    print(NUMBER)
    NUMBER -= 3
    
    
    

