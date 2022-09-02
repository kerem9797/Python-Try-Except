# USER LOGIN APPLICATION

from logging import exception

def login(username,password):
    import re
    if not re.search('[@]',username):
        raise exception("Username must contain '@' ")
    elif re.search('\s',username):
        raise exception('Username does not contain spaces')
    elif len(password)<7:
        raise exception('Password must contain at least 7 characters')
    elif not re.search('[0-100]',password):
        raise exception('Password must contain number')
    elif not  re.search('[a-z]',password):
        raise exception('Password must contain lowercase letters')
    elif re.search('\s',password):
        raise exception('Password does not contain spaces')
    else:
        print('Username and password are true')
        print('Login Successful...')
username='keremkarakas123@gmail.com'
password='abcdef12345'
due=3        
while True:
    try:
        username=input('Username:')
        password=input('Password:')
        login(username,password)
    except:
        print('Username or password is false')
        due-=1
        continue
    finally:
        if(username=='keremkarakas123@gmail.com')and(password=='abcdef12345'):
            break
        if(due==0):
           print('You have no more rigths')
           break

           




            
