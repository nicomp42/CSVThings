# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from utilsPackage.utils import *

# Call the function and store what it returns 
#  in a variable called data
if __name__ == "__main__":
    data = read_CSV_file()
    print("# of rows in dataset:", len(data))
    # Print the first and last rows in data
    print(data[0])
    print(data[-1])
    # I want a list comprehension expression to pull out all the Collision Types into a set.
    # Modify this expression to exclude the blank collision type
    collisionTypes = {myData[6] for myData in data}
    print("# of collision type:", len(collisionTypes))
    print(collisionTypes)
    
    
