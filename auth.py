import hashlib
from database import supabase
def hashFunction(password):
    hashName=hashlib.sha256(password.encode())
    hexa=hashName.hexdigest()
    return hexa
def signup(firstname,lastname,username,password,confirmpassword):
    result=supabase.table('users').select('username').eq('username',username).execute()
    if result.data:
        return "UserName already exist!"
    if password==confirmpassword:
        hashed=hashFunction(password)
        supabase.table('users').insert({
            'firstname':firstname,'lastname':lastname,'username':username,'password':hashed
        }).execute()
        return "Signup Successful!"
    else:
        return "Password do not match"
def login(username,password):
    hashed=hashFunction(password)
    result=supabase.table('users').select('*').eq('username',username).eq('password',hashed).execute()
    if result.data:
        return "Login Successful"
    return "Invalid username or password"

