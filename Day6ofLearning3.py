print('get a input for username and password and validate it using return')
s_name='Alice@123'
s_password='67870'

username=input('enter username: ')
password=input('enter password: ')
def validate():
    if username==s_name and password==s_password:
        return True
    elif password!=s_password:
        return'incorrect password'
    elif username!=s_name:
        return 'incorrect username'
    else:
        return False
a=validate()
print(a)
