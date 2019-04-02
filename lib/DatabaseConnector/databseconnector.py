import mysql.connector as mysql

class DatabaseConnection:

    def __init__(self,host='localhost',database='newcustomer', user='root',password='root'):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.conn=None
        self.cursor=None

    def __enter__(self):
        self.conn=mysql.connect(host=self.host,database=self.database,user=self.user,password=self.password)

        if(self.conn.is_connected()):
            print("Connected to database")
        else:
            print("not connected")

        self.cursor=self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if self.conn.is_connected():
             print('Connected to MySQL database')
        else:
            print("succssfully closed database connection")


    def execute_query1(self, query):
        print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def execute_query2(self,query):
         self.cursor.execute(query)
         result=self.cursor.fetchall()
         return result










