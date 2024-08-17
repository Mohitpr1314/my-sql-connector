from DBhelper import DBhelper
import sys



class Flipkart:
    def __init__(self):
        self.db = DBhelper()
        self.menu()


    def menu(self):
        user_input = int(input('''
        1. Enter 1 for registration
        2. Enter 2 for login
        3. Enter 3 for exit
'''))
        if user_input == 1:
            self.register()
        elif user_input == 2:
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input('Enter your name : \n')
        email = input('Enter your email : \n')
        password = input('Enter your password : \n')

        response = self.db.register(name, email, password)
        if response:
            print('Registration Successful')
        else:
            print('Registration failed')

        self.menu()



obj  = Flipkart()





