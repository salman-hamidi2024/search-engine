import os
import re
os.system('clear')
user_input = input("what do you want: ")

path = os.listdir("dickens")

for file_name in path:

    full_file = os.path.join('dickens',file_name)
    
    open_ai = open(full_file,"r")
    data = open_ai.read()
    open_ai.close()
    search  = re.search(full_file,user_input)
    print(f"your search found in {full_file}")
    print("content:")
    print(data)