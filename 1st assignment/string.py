import os

def create_string(filename, location):
    print(filename, location)
    if os.path.isfile(location+'/'+filename):
        print("the file exists in directory")
        with open(filename, 'w+') as file:
            val  = input("enter the string you wanna input ")
            file.write(val)

        with open(filename,'r+') as file:
            text = file.read()
            print(f'youve entered the string as  = {text}')
            original = input("enter the string you want to replace ")
            replace = input("enter the specific word you want to remove ")
            text = text.replace(original , replace)
        
        with open(filename, 'w') as file:
            file.write(text)
        
        with open(filename, 'r') as file:
            print(file.read())
    
    else:
        print("file doesnt belong in this directory")
        with open(filename, 'w+') as file:
            val  = input("enter the string you wanna input ")
            file.write(val)
        with open(filename,'r+') as file:
            text = file.read()
            print(f'youve entered the string as  = {text}')
            original = input("enter the string you want to replace ")
            replace = input("enter the specific word you want to remove ")
            text = text.replace(original , replace)
        
        with open(filename, 'w') as file:
            file.write(text)
        
        with open(filename, 'r') as file:
            print(file.read())
    
    

filename = 'assignment.txt'
location = os.getcwd()
create_string(filename, location)

