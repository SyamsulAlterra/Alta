import re

database=[
    {'email':'johndoe@gmail.com','password':'123456'},
    {'email':'johndoe@yahoo.co.id','password':'123456'},
    {'email':'john_doe@gmail.com','password':'asdfasdfds'}
]

def validasiLogin(email,password):
    output={}
    output['pesan']=""
    output['status']=False
    emailPattern="(\w+@[a-z]+([.][a-z]+)+)"
    passwordPattern="[a-zA-Z0-9]{6,10}"

    checkEmail=re.findall(emailPattern,email)
    checkPass=re.findall(passwordPattern,password)

    if len(checkEmail)==0:
        output['pesan']='email tidak valid'
        return output
    elif not checkPass:
        output['pesan']='password tidak valid'
        return output

    for item in database:
        if email == item['email']:
            if password == item['password']:
                output['pesan']=[]
                output['status']=True
                return output
            else:
                output['pesan']='password salah'
                return output
            
    output['pesan']='email tidak ada di database'
    return output

print(validasiLogin('johndoe@gmail.com','123456'))
# {'pesan':[], 'status':True}
print(validasiLogin('jane@gmail.com','1245'))
# {'pesan':'password tidak valid', 'status':False]}
print(validasiLogin('johndoe_gmail.com','123456'))
# {'pesan':'email tidak valid', 'status':False]}
print(validasiLogin('johndoe@yahoo.co.id','12abcd'))
# {'pesan':'password salah', 'status':False]}
print(validasiLogin('john_doe@gmail.com','asdfasdfds'))
# {'pesan':[], 'status':False]}


