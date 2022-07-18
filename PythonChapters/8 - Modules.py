import sales
from sales import calc_shipping, calc_tax
8 - MODULES
== == == == == == == == == == == == == = 1 - Creating Modules == == == == == == == == == == == == == == ==


# another way to import is using this clause:

# and them using the same module as an function
sales.calc_tax

shipping = calc_shipping()

calc_tax()


doc = shipping.__file__

print(doc)
