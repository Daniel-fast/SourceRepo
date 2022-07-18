
from ctypes import LibraryLoader


9 - PYTHON STANDARD


== == == == == == == == == == == ==  2- Working With Paths == == == == == == == == == == == ==

from pathlib import Path

https://docs.python.org/3/library/pathlib.html

Path("C:\\Program Files\\Microsoft")

#We can prefix it with " r" that stands for Raw and - this way, we can azssign the path in a normal way
# with the "r - Raw, we get rid of the second backslash!
Path(r"C:\Program Files\Microsoft")

#Now - if you are on Mac or Linux, you can create an absolute path like:
Path("/usr/local/bin")

#We can create the path object that represents the current folder.
Path()


#we can use Path to represent the current forlder like this:
Path("ecommerce/__init__.py")

# we can also combine objects using slash to combine with another path

Path() / Path("ecommerce")

# Or we can also combine a path object with a string

Path() / "ecommerce" / "__init__.py" # and again, combine with another string

#We can get the path of the current user
Path.home() 

# All these are examples of using Path

path = Path("ecommerce/__init__.py")
path.exists() # to check if thew path really exists
path.is_file() # to check if has the file
path.is_dir() # to check if it is just a directory

print()
print("Executing")
print()
print(path.name) #so, it returns olnly the filename of the path

print()
print("path.stem - prints only the name, without extention:",path.stem) # __init__
print()
print("path.suffix - prints the extention:",path.suffix) # .py
print()
print("path.parent - prints the parent path:",path.parent) #ecommerce
print()
print("path.absolute - prints the absolute path:",path.absolute()) #C:\Repos\source\Python\app\ecommerce\__init__.py
print()
path = path.with_name("file.txt") # ecommerce\file.txt
print("We can use the clause with:  path.with_name(´file.txt´): ",path)
print()
print("we can also get the absolute path of this new object path:",path.absolute()) ## C:\Repos\source\Python\app\ecommerce\file.txt - of course thi file doesn´t exists 
print()
path = path.with_suffix(".png") # ecommerce\file.txt
print("We can use the clause with_suffix:  path.with_suffix(´.png´): ",path) #ecommerce\file.png
# once again, note we are not renaming the file, we are only representing a path object 
print()



== == == == == == == == == == == ==  4- Working with Files  == == == == == == == == == == == ==


Example one - working with the time module

print() 
path = Path("ecommerce/__init__.py")
print(path.exists())
print()   
print("st_ctime:", (ctime(path.stat().st_ctime)), " st_mtime:", (ctime(path.stat().st_mtime)))
print()   
print(path.read_bytes())   
os.stat_resul3206, st_ino=2814749path.stat().st_ctime767340399, st_dev=3029078300, st_nlink=1, st_uid=0, st_gid=0, st_size=43, st_atime=1656902152, st_mtime=1656722358, st_ctime=1656598268)
st_atime=1656902152 = seconds after epic that is the start of the computer 



Example two - using the shutil module + my program to create, check and delet files

print() 
print ("Executing part two - using shutil module")
print()
ref1 = Path("ecommerce/shopping/consumer_car/salescar.py")
ref2 = Path() / "salescar_copy.py"

if ref2.exists() == True:
    print()
    print("Path:", ref2, " exists")
    print()
    print("st_ctime:", (ctime(ref2.stat().st_ctime))," st_mtime:", (ctime(ref2.stat().st_mtime)))
    print()
    print("going to delete with unlink() method")
    print()
    ref2.unlink()
    if ref2.exists == True:
        print("unlink() method doesn´t worked")
        print()
    else:
        print("file:", ref2, "deleted with unlink() method")
        print()
    

if ref1.exists() == True:
    print("First if ok, ref1 exists:", ref1)
    shutil.copy(ref1, ref2)
    path2 = Path() / "salescar_copy.py"
    if path2.exists() == True:
        print()
        print("copy succeeded, path:", path2, " exists")
        print()
        print("st_ctime:", (ctime(path2.stat().st_ctime)), " st_mtime:", (ctime(path2.stat().st_mtime)))
        print()
        print("Yessssssss!!!!!!")
        
    else:
        print("Copy failed, check again")
else:
    path2 = Path("/salescar_copy.py")
    print("Path:", path2, " doesn´t exist")
    
print()


== == == == == == == == == == == ==  5- Working with Zip Files - crea == == == == == == == == == == == ==
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


== == == == == == == == == == == ==  5- Working with Zip Files - Extracting  == == == == == == == == == == == ==
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
    
    

== == == == == == == == == == == ==   7- Working with JSON Files -  == == == == == == == == == == == ==
JSON stands for JavaScript Object Notation.

Creating a JSON file

import json
from pathlib import Path
from re import M
    

movies = [
    {"id": 1, "title": "Terminator", "year": 2000 },
    {"id": 2, "title": "Midnight in Paris", "year": 2009 },
    {"id": 3, "title": "How I met your Mother", "year": 2008 },
    {"id": 4, "title": "Avatar", "year": 2004 },
    {"id": 5, "title": "Top Gun", "year": 1987 },
    {"id": 6, "title": "Maverick", "year": 1994 }
]    
 

data = json.dumps(movies) #this creates an object string (for the data variable)
#print(data)

Path("movies.json").write_text(data)

print("JSON file created")


Reading a JSON file

import json
from pathlib import Path
from re import M
    


data = Path("movies.json").read_text() # This will read the JSON file and put it as a string in data

movies = json.loads(data) # This will creates a Dictionary with the string values from data (parse the values)


print("Movies dictionary", movies)
print("Movies dictionary", movies)
print()
print("JSON dictionary created")

print()
print(movies[0]) # this will print the values of key 0 (the first)
print()
print("Movie:", movies[1] ["title"]) # this will print only the title value from the second record


 == == == == == == == == == == == ==   8- Working with a SQLite Database -  == == == == == == == == == == == ==
# creating and writing in a SQL lite DB

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

#connection = sqlite3.connect("db.sqlite3") #this crerates a connection and if the DB doesn´t exist, no problem, this method will create for us. Next we will add it to the "connection" object
#this will return a connection object, this connection object, similiar a files should be closed when you´re done with it. So the better approach is to use the "with" statement
# and them get the connection here

# lets convert this: ' movies = json.loads(Path("movies.json").read_text()) ' into this:

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)" # we will use three question marks spareted by a comma (because we have the fields)
    # The question marks are placeholders for the values we are going to put here
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
    

# reading the SQL data in SQLLITE3

import sqlite3
import json
from pathlib import Path



with sqlite3.connect("db.sqlite3") as conn: #we still need this connection
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command) # this will return a 'cursor' because when you read data from a database you´will get a cursor object that is iterable
    
    # for row in cursor:
    #     print(row) 
    
    movies = cursor.fetchall() # when we use the fetchall function, we don´t need to iterate over the movies so we can comment the for loop
    print(movies) # now we get a list of tuples [(1, 'Terminator', 2000), (2, 'Midnight in Paris', 2009), (3, 'How I met your Mother', 2008), (4, 'Avatar', 2004), (5, 'Top Gun', 1987), (6, 'Maverick', 1994)]



== == == == == == == == == == == ==   9- Working with Timestamps -  == == == == == == == == == == == ==
import time

print(time.time())

# result = 1657373441.895803   this float number representes the amount of seconds since the start of the operational system,
# In unix systems it started in 01/01/1970 - (called - Epic Time)

def send_emails(delta):
    for i in range(delta):
        pass
    

print()
start = time.time()
send_emails(100000)
end = time.time()

duration = end - start

print(duration)
print()


 == == == == == == == == == == == ==   10- Working with DateTimes  == == == == == == == == == == == ==
from datetime import datetime
import time

#https://docs.python.org/3/library/datetime.html



# using the clause: ´import datetime` makes us to use for example: datetime.datetime  (thats ugly). Lets use: from datetime import datetime
# 

# dt = datetime.now()


dt = datetime.strptime("2018/01/01", "%Y/%m/%d")

print(f"{dt.year}/{dt.month}")


== == == == == == == == == == == ==    11- Working with Time Deltas  == == == == == == == == == == == ==
from datetime import datetime


from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)

dt2 = datetime.now()

duration = dt2 - dt1

print(duration)
print()
print("days: ", duration.days)
print()
print("seconds:", duration.seconds)
print()
print("microseconds: ", duration.microseconds)
print()
print("total_seconds", duration.total_seconds())
print()

result
1651 days, 12:23:18.752735

days:  1651

seconds: 44598

microseconds:  752735

total_seconds 142690998.752735



using the timedelta function

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)

dt2 = datetime.now()

duration = dt2 - dt1

print(duration)
print()

result
2018-01-02 00:16:40
1650 days, 12:13:10.002146


== == == == == == == == == == == ==    12- Generating Random Values  == == == == == == == == == == == ==
https://docs.python.org/3/library/random.html
import random
import string


print("Random value:", random.random()) #Random value: 0.4731568264245445 (brings a float number between 0 and 1)
print()
print("Random integer value:", random.randint(1, 10)) #Random integer value: 3
print()
print("Random choice:", random.choice([1, 2, 3, 4])) #Random choices: 3 (any value in the array )
print()
print("Random choiceS:", random.choices([1, 2, 3, 4], k=4)) #Random choiceS: [2, 3, 3] - second time when k=4: Random choiceS: [1, 1, 1, 1]
print()
print("Let´s try a password:", random.choices("abcdefghijklmnopqrstuvxywv", k=6)) #Let´s try a password: ['r', 'n', 'v', 'b', 'd', 'r']
print()
print("Let´s suppose we want a string instead an array:") #Let´s try a password: ['r', 'n', 'v', 'b', 'd', 'r']
print("".join(random.choices("abcdefghijklmnopqrstuvxywv", k=6))) #crvwuv - (we could have used a ',' (comma) instead of a empty string - this would return: c,r,v,w,u,v)
print()
print(string.ascii_letters)
print()
print("".join(random.choices(string.ascii_letters + string.digits, k=12,))) # HGUkV1glC3BU
print("we can shuffle:")
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers) # [1, 3, 4, 2]  / [4, 3, 1, 2] / [4, 2, 3, 1]

print("Using weights")
sample_lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choices(sample_lists, weights=(90, 20, 30, 40, 50, 30, 20, 10, 5, 1),k=12,)) #[0, 2, 0, 4, 0, 4, 0, 1, 0, 2, 3, 0]


# Randomly select elements from list without repetition in Python
  
# list of items
List = [10, 20, 30, 40, 50, 40, 30, 20, 10]
  
# using the sample() method
UpdatedList = random.sample(List, 3)
  
# displaying random selections from 
# the list without repetition
print(UpdatedList)

== == == == == == == == == == == ==   13- Opening the Browser  == == == == == == == == == == == ==
import webbrowser

print("Tasks completed successfully!")

webbrowser.open("https://www.google.com")


    