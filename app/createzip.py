# == == == == == == == == == == == ==  5- Working with Zip Files - crea == == == == == == == == == == == ==
from pathlib import Path
from zipfile import ZipFile # from the zipfile module, lets import the ZipFile class


with ZipFile("files.zip", "w") as zip: # Let´s create the ZipFile object e associate it to a variable zip / remember that after, we put the "with" statement
# Let´s create the object Path referencing the dir and with the rglog method to recursely find all the files 
# in the directory and all is true. And, as you know it returns a generator, so we iterate over it
# so we use the for statment; 

    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
#zip.close()
# Finally we should call the close method  zip.close()   Now, if something goes wrong here chances are the statment may not be called,
# so we should either use a "try finally block, or the "with" statement which is shorter and cleaner.





 




