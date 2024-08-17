import sys
import  mysql.connector



class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="mohit")
            self.mycursor = self.conn.cursor()
        except:
            print('Error, DAtabase is not connected')
            sys.exit(100)
        else:
            print('Database is connected')

    def register(self, name, email, password):
        try:
            self.mycursor.execute('''
                INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')'''.format(name, email, password)
            )
            self.conn.commit()
        except:
            return -1
        else:
            return 1
