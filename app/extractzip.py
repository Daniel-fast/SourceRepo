# == == == == == == == == == == == ==  5- Working with Zip Files  == == == == == == == == == == == ==
from pathlib import Path
from zipfile import ZipFile # from the zipfile module, lets import the ZipFile class


with ZipFile("files.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("ecommerce/5348d704-6f5b-4716-8c54-200176f386d4.jpg")
    print("File size:", info.file_size)
    print()
    print("Compress size:", info.compress_size)
    print()
    print("Compress type:", info.compress_type)
    print()
    print("Hash:", info.__hash__)
    zip.extractall("daniel")
    



 




