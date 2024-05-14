from cryptography.fernet import Fernet

'''
# Define a function to generate and write an encryption key to a file
def write_key():
     # Generate a new encryption key using the Fernet library
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        # Write the generated key to the file
        # Since the key is binary data, it's written directly to the file
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

#define a fucntion 
def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("Username: ",user,"| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name= input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f: #f - name of the file
        f.write(name + " | "+ fer.encrypt(pwd.encode()).decode() + "\n")
        
        
       # modes
       # w - write (overrite this file into a complete new one, ex: make a new file ignoring the existing one)
       # r - read (all you can do is read the file)
       # a - append (add somthing to the end of the existing file, and create a new file if the file does not exists)
       
while True:
    mode = input ("would you like to add a new password or view an existing one? (view/add/ and press q to quit) ").lower()
    
    if mode == "q":
        break

    if mode =="view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode" )
        continue #bring you back to the top to continue the loop
