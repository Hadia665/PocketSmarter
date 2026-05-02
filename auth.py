import hashlib
import csv
import os
def hashFunction(password):
    hashName=hashlib.sha256(password.encode())
    hexa=hashName.hexdigest()
    return hexa
def signup(firstname,lastname,username,password,confirmpassword):
    if os.path.exists('output.csv'):
        with open('output.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[2]==username:
                    return "UserName already exist!"
    if password==confirmpassword:
        hashed=hashFunction(password)
        with open ('output.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow([firstname,lastname,username,hashed])
        return "Signup Successful!"
    else:
        return "Password do not match"
def login(username,password):
    if not os.path.exists('output.csv'):
        return "No users found"
    with open('output.csv','r',newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if row[2]==username and row[3]==hashFunction(password):
                return "Login Successful"
        return "Invalid username or password"

